from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.postgres import fields as pg
from cerberus import Validator
from .schema import (
    work_schema,
    page_schema,
    event_schema,
    person_schema,
    organization_schema,
    place_schema,
)


# todo:
    # PyDoc for classes
    # help_text for fields


class Base(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    modified_on = models.DateTimeField(
        auto_now=True,
    )


class License(Base):
    title = models.CharField(
        max_length=250,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    url = models.URLField(
        blank=True,
    )

    def __str__(self):
        return self.title


class Image(Base):
    schema = 'http://schema.org/ImageObject'
    title = models.CharField(
        max_length=250,
    )
    ASPECTS = (
        ('main', 'Main'),
        ('recto', 'Recto'),
        ('verso', 'Verso'),
        ('detail', 'detail'),
        ('signature', 'signature'),
    )
    aspect = models.CharField(
        max_length=25,
        choices=ASPECTS,
        default='main',
    )
    checksum = models.CharField(
        max_length=250,
        unique=True
    )
    source = models.ForeignKey('Record',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Category(Base):
    class Meta:
        unique_together = (
            # ("value", "vocabulary"),
            ("value", "parent"),
        )

    # CATEGORIES = {
    #     'event': [
    #         'course',
    #         'exhibition',
    #         'performance',
    #         'reception',
    #         'residency',
    #         'workshop',
    #     ],
    #     'work': [
    #         'article',
    #         'book',
    #         'installation',
    #         'photograph',
    #         'sculpture',
    #         'visual artwork',
    #         'website',
    #         'vocabulary',
    #         'license',
    #     ],
    #     'person': [
    #         'artist',
    #         'writer',
    #         'architect',
    #         'filmmaker',
    #         'curator',
    #         'gallerist',
    #         'professor',
    #         'manager',
    #     ],
    #     'organization': [
    #         'archive',
    #         'association',
    #         'company',
    #         'consortium',
    #         'foundation',
    #         'library',
    #         'museum',
    #         'school',
    #     ],
    #     'page': [
    #         'article',
    #         'review',
    #         'collection',
    #         'tour',
    #     ],
    #     'place': [
    #         'spot',
    #         'area',
    #         'island',
    #         'neighborhood',
    #         'city',
    #         'county',
    #         'region',
    #         'state',
    #         'country'
    #     ],
    # }

    parent = models.ForeignKey('self',
        related_name='children',
        blank=True,
        null=True,
    )
    # vocabulary = models.ForeignKey('Record')
    value = models.CharField(
        max_length=250,
    )
    description = models.TextField(
        blank=True,
        null=True,
        )

    def __str__(self):
        return self.value


class Tag(Base):
    value = models.SlugField(
        unique=True
    )
    # vocabulary = models.ForeignKey('Record')
    description = models.TextField(
        blank=True,
        null=True,
        )

    def __str__(self):
        return self.value


class Identifier(Base):
    value = models.CharField(
        max_length=250,
    )
    record = models.ForeignKey('Record')

    def __str__(self):
        return self.value


class Relation(models.Model):

    PREDICATES = (
        # item-level
            # relations flow in this direction, when possible
                # Event
                # Work
                # Organization
                # Person
                # Place
                # Page

            # event
            # (('has_event'), ('has event')), # reverse

            # work
            # (('has_work'), ('has work')), # reverse

            # person/organization
            (('has_contributor'), ('has contributor')),
            (('has_creator'), ('has creator')),
            (('has_curator'), ('has curator')),
            (('has_employee'), ('has employee')),
            (('has_exhibitor'), ('has exhibitor')),
            (('has_friend'), ('has friend')),
            (('has_member'), ('has member')),
            (('has_organizer'), ('has organizer')),
            (('has_owner'), ('has owner')),
            (('has_parent'), ('has parent')),
            (('has_producer'), ('has producer')),
            (('has_publisher'), ('has publisher')),
            (('has_affiliation'), ('has affiliation')),
            (('has_spouse'), ('has spouse')),
            (('has_venue'), ('has_venue')),

            # place
            (('located_at'), ('located at')),
            (('started_at'), ('started at')),
            (('ended_at'), ('ended at')),
            (('born_at'), ('born at')),
            (('died_at'), ('died at')),

            # generic
            (('part_of'), ('part of')),
            (('same_as'), ('same as')),
            (('same_as'), ('same as')),

        # meta-level
        (('has_record_source'), ('has record source')),
        (('has_record_parent'), ('has record parent')),
    )
    subject = models.ForeignKey('Record',
        related_name='relation_subject',
        on_delete=models.CASCADE,
    )
    predicate = models.CharField(
        choices=PREDICATES,
        max_length=25,
    )
    dobject = models.ForeignKey('Record',
        related_name='relation_direct_object',
        on_delete=models.CASCADE,
    )
    properties = pg.JSONField(
        blank=True,
        null=True
    )
    dates = pg.DateTimeRangeField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return '( {} )-[ {} ]->( {} )'.format(self.subject, self.predicate, self.dobject)


class Record(Base):
    class Meta:
        ordering = [
            '-created_on',
        ]

    schema = 'http://schema.org/Thing'

    LABELS = (
        (('event'), ('event')),
        (('work'), ('work')),
        (('person'), ('person')),
        (('organization'), ('organization')),
        (('page'), ('page')),
    )

    related = models.ManyToManyField('self',
        through='Relation',
        through_fields=('subject', 'dobject'),
        symmetrical=False,
        blank=True
    )
    slug = models.SlugField(
        unique=True,
    )
    label = models.CharField(
        max_length=25,
        choices=LABELS,
    )
    properties = pg.JSONField(
        blank=True,
        null=True
    )
    status = models.NullBooleanField(
        default=None,
    )
    license = models.ForeignKey('License',
        related_name='records_licensed',
        default=1,
    )

    # classification
    tags = models.ManyToManyField('Tag',
        blank=True,
    )
    categories = models.ManyToManyField('Category',
        blank=False,
    )
    images = models.ManyToManyField('Image',
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )
    is_featured = models.BooleanField(
        default=False,
    )
    is_approved = models.BooleanField(
        default=False,
    )
    is_web_public = models.BooleanField(
        default=True,
    )

    # methods
    def __str__(self):
        return '{}: {}'.format(self.label, self.slug)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def clean(self):
        # Make sure properties validate correctly.
        schemas = {
            'event': event_schema,
            'work': work_schema,
            'person': person_schema,
            'organization': organization_schema,
            'page': page_schema,
        }
        schema = schemas[self.label]
        if self.properties:
            v = Validator(schema)
            if not v.validate(self.properties):
                raise ValidationError(
                    {'properties': 'Properties do not fit {} schema.'\
                    .format(self.label)})



    def name(self): # title
        pass

    def age(self):
        pass

    def citation(self):
        pass

    def date(self):
        pass

    def get_absolute_url(self):
        pass

    def location(self):
        pass

    def address(self):
        pass

    def distance(self):
        pass

    def duration(self): # lifespan
        pass



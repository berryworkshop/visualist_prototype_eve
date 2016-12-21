from django.contrib import admin
from cms.models import (
    Name, Article, Description,
    Identifier, Language, License, Link, Log, Page, Record, RecordSet,
    Relation, Subject, Term, Unit, Vocabulary)
from tour.models import (
    Place, Space, Venue, State, City, Neighborhood, PostalCode)
from aggregator.models import (
    Source, Service, RightSet)
from archive.models import (
    File, Image, Document, Video, ArchiveEvent)
from timeline.models import (
    Period, Event, Moment)
from catalog.models import (
    Work, Dimension, Medium, Genre, Thing)
from crosswalk.models import (
    Schema)
from directory.models import (Person, Organization,
    Account, Address, Email, Phone, Website, HourSet)

admin.site.register(Account)
admin.site.register(Address)
admin.site.register(ArchiveEvent)
admin.site.register(Article)
admin.site.register(City)
admin.site.register(Description)
admin.site.register(Dimension)
admin.site.register(Document)
admin.site.register(Email)
admin.site.register(Event)
admin.site.register(File)
admin.site.register(Genre)
admin.site.register(HourSet)
admin.site.register(Identifier)
admin.site.register(Image)
admin.site.register(Language)
admin.site.register(License)
admin.site.register(Link)
admin.site.register(Log)
admin.site.register(Medium)
admin.site.register(Moment)
admin.site.register(Name)
admin.site.register(Neighborhood)
admin.site.register(Organization)
admin.site.register(Page)
admin.site.register(Period)
admin.site.register(Person)
admin.site.register(Phone)
admin.site.register(Place)
admin.site.register(Record)
admin.site.register(RecordSet)
admin.site.register(Relation)
admin.site.register(RightSet)
admin.site.register(Schema)
admin.site.register(Service)
admin.site.register(Source)
admin.site.register(Space)
admin.site.register(State)
admin.site.register(Subject)
admin.site.register(Term)
admin.site.register(Thing)
admin.site.register(Unit)
admin.site.register(Venue)
admin.site.register(Video)
admin.site.register(Vocabulary)
admin.site.register(Website)
admin.site.register(Work)
admin.site.register(PostalCode)
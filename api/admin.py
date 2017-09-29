from django.contrib import admin
from api.models import (
    Identifier,
    Image,
    License,
    Category,
    Record,
    Relation,
    Tag,
    # Category,
)

admin.site.register(Identifier)
admin.site.register(Image)
admin.site.register(License)
admin.site.register(Category)
admin.site.register(Record)
admin.site.register(Relation)
admin.site.register(Tag)
# admin.site.register(Category)

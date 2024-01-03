from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Resource,Site,Record

admin.site.register(Site)
admin.site.register(Resource)
admin.site.register(Record)

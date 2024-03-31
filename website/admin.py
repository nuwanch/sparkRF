from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Resource,Site,Record,PhyInfo, AntennaTable, RHTable, CombinerTable, FilterTable, BBPTable, MPTTable

admin.site.register(Site)
admin.site.register(Resource)
admin.site.register(Record)
admin.site.register(PhyInfo)
admin.site.register(AntennaTable)
admin.site.register(RHTable)
admin.site.register(CombinerTable)
admin.site.register(FilterTable)
admin.site.register(BBPTable)
admin.site.register(MPTTable)



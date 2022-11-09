from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from .models import Profile

admin.site.register(Profile, admin.OSMGeoAdmin)
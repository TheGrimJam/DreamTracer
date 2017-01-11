from django.contrib import admin
from tracer.models import UserProfile, Dream, Locations, Themes


admin.site.register(UserProfile)
admin.site.register(Dream)
admin.site.register(Locations)
admin.site.register(Themes)

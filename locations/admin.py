from django.contrib import admin
from .models import City, District, Ward, Manager, Location

# Register your models here.

admin.site.register(City)
admin.site.register(District)
admin.site.register(Ward)
admin.site.register(Manager)
admin.site.register(Location)
from django.contrib import admin
from . models import Place,Team # we need to import place table from models.py

# Register your models here.
# here we need to load file of tables ie.models.py

admin.site.register(Place) #to get/register this table 'place' in admin site
admin.site.register(Team)
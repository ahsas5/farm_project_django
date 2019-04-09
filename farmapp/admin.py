from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Farmer)
admin.site.register(models.Farm)
admin.site.register(models.Schedule_detail)

from django.contrib import admin

from . import models
admin.site.register(models.Topic)
admin.site.register(models.Comment)
admin.site.register(models.Category)

# Register your models here.

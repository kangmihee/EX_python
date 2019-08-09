from django.contrib import admin
from mysangpum.models import Sangdata

# Register your models here.
class SangdataAdmin(admin.ModelAdmin):
    list_display = ('code','sang','su','dan')

admin.site.register(Sangdata, SangdataAdmin)
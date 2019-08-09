from django.contrib import admin
from myapp.models import Survey


# Register your models here.

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('rnum','gender','age','co_survey')

admin.site.register(Survey, SurveyAdmin) 

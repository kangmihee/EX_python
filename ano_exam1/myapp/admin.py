from django.contrib import admin
from myapp.models import Starbucks


# Register your models here.

class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id','job','gender','survey')

admin.site.register(Starbucks, SurveyAdmin) 
from django.contrib import admin
from examapp.models import Score

# Register your models here.
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'irum', 'kor', 'eng')
    
admin.site.register(Score, ScoreAdmin)
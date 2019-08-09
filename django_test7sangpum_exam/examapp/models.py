from django.db import models

# Create your models here.
class Score(models.Model):
    irum = models.CharField(max_length = 10)
    kor = models.IntegerField()
    eng = models.IntegerField()
    
    class Meta:
        ordering = ('id',)
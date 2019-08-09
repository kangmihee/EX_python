from django.db import models

# Create your models here.

class Guest(models.Model):
    #myno = models.AutoField(auto_created = True, primary_key = True)  # 옵션설정
    title = models.CharField(max_length=50)
    content = models.TextField()
    regdate = models.DateTimeField()


    class Meta:
        #ordering = ('title',) # title별 sort
        ordering = ('-id',)    # 내림차순으로 정렬
        
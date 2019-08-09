from django.db import models

# Create your models here.

class Article(models.Model):
    code = models.CharField(max_length=10)  # PK를 옵션으로 만들어주지않으면 자동 생성
    name = models.CharField(max_length=20) 
    price = models.IntegerField()    # 고정크기
    pub_date = models.DateTimeField()
    
    
class Article2(models.Model):
    name = models.CharField(max_length=20) 
    tel = models.CharField(max_length=20)
    
    

        
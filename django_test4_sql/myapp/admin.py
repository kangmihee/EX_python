from django.contrib import admin
from myapp.models import Article, Article2

# Register your models here.

#admin.site.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'price', 'pub_date')

class ArticleAdmin2(admin.ModelAdmin):
    list_display = ('id', 'name', 'tel')
 
admin.site.register(Article, ArticleAdmin) 
admin.site.register(Article2, ArticleAdmin2)   
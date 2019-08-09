from django.contrib import admin
from myapp.models import Jikwon

# Register your models here.

class JikwonAdmin(admin.ModelAdmin):
    list_display = ('jikwon_no','jikwon_name','buser_num','jikwon_jik',
                    'jikwon_pay','jikwon_ibsail','jikwon_gen','jikwon_rating')

admin.site.register(Jikwon, JikwonAdmin) 

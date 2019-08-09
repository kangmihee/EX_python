# app에 만들어진 urls.py

from django.urls import path
from myapp import views

urlpatterns = [
    path('kbs', views.worldFunc),   # 값이 있을경우 'http://127.0.0.1:8000/world/kbs' 로 가야한다 
    
    ]
from django.urls import path
from mysangpum import views

urlpatterns = [
    path('list/', views.ListFunc), 
    path('insert/', views.InsertFunc),
    path('insertok/', views.InsertokFunc),
    path('update/', views.UpdateFunc),
    path('updateok/', views.UpdateokFunc),
    path('delete/', views.DeleteFunc),
    
]
from django.urls import path
from myapp import views

urlpatterns = [
    path('insert/', views.InsertFunc),
    path('insertok/', views.InsertOkFunc),
    path('list/', views.ListFunc),
]
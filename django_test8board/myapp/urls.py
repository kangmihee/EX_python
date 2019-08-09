from myapp import views
from django.urls import path


urlpatterns = [
    path('list/', views.ListFunc),
    path('insert/', views.InsertFunc),
    path('insertok/', views.InsertokFunc),
    path('update/', views.UpdateFunc),
    path('updateok/', views.UpdateokFunc),
    path('delete/', views.DeleteFunc),
    path('deleteok/', views.DeleteokFunc),
    path('search/', views.SearchFunc),
    path('content/', views.ContentFunc),
    path('reply/', views.ReplyFunc),
    path('replyok/', views.ReplyokFunc),
    
    ]
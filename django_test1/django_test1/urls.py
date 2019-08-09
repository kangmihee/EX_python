"""django_test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views (방법1)
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views (방법2)
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf (방법3)
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.indexFunc, name="index"),  # 방법 1 (다이렉트로 넘어감)
    path('hello', views.hello),               # 방법 2
    path('world/', include('myapp.urls')),    # 방법 3 (/를 넣어줘서 위임시킴)
    
    
]

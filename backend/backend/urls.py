"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include               
from rest_framework import routers                 
from Products import views 
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


#router = routers.DefaultRouter()                   
#router.register(r'Products', views.ProductsView, 'Products')  

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('api/', include(router.urls)),
    path('Products/', include('Products.urls')),
    path('User/', include('user.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
]

urlpatterns += staticfiles_urlpatterns()
from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLPattern
from .import views


urlpatterns=[
       path('register/',views.register),
       path('login/',views.login,name='login'),
       path('login/',views.logout,name='logout'),
       

]

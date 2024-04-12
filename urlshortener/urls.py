from django.contrib import admin
from django.urls import path,include
from shortener.views import index,list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("shortener.urls",namespace="shortener"),name="index"),
]
 
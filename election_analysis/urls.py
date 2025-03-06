from django.contrib import admin
from django.urls import path,include
from analysis.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('analysis/',include('analysis.urls')),
]

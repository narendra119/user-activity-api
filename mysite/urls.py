"""To route the urls to their respective views
"""
from django.contrib import admin
from django.urls import path
from activity_periods_api import views


urlpatterns = [
    
    path('', views.work_view, name = 'test'),
    path('admin/', admin.site.urls), 
    
]
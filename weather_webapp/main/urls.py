from django.contrib import admin
from django.urls import path
from main.views import AboutView, IndexView
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
]
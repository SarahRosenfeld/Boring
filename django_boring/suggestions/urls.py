from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='suggestions-home'),
    path('about/', views.about_page, name='suggestions-about'),
]
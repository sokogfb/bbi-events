from django.urls import path

from home_app import views

app_name = 'home'
urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('index/', views.index, name='index'),
]

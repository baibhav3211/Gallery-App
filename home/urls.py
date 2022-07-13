from django.urls import path
from . import views

urlpatterns = [
    path('', views.getImages, name='getImages'),
    path('create/', views.createImage, name='createImage'),
    path('search/', views.search, name='search'),
    path('image/<slug:slug>/', views.getImage, name='getImage'),
    path('update/<str:slug>/', views.editImage, name='editImage'),
    path('delete/<slug:slug>/', views.deleteImage, name='deleteImage'),
]
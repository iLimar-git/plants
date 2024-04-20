from django.urls import path
from . import views

urlpatterns = [
    path('', views.plant_list, name='plant_list'),
    path('add/', views.add_plant, name='add_plant'),
    path('delete/<int:pk>/', views.delete_plant, name='delete_plant'),
    path('add_gallery/', views.add_gallery, name='add_gallery'),
    path('delete_gallery/<int:pk>/', views.delete_gallery, name='delete_gallery'),
    path('gallery/', views.gallery, name='gallery'),
]


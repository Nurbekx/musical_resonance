from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('search/', views.search, name='search'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guides/', views.guides, name='guides'),
    path('videos/', views.videos, name='videos'),
    path('tests/', views.tests, name='tests'),
    path('music/', views.music, name='music'),
    path('guide/<int:pk>/', views.guide_detail, name='guide_detail'),
    path('books/', views.books, name='books'),
]
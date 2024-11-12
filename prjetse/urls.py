from django.contrib import admin
from django.urls import path
from .views import *
from django.views.generic import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(pattern_name='art_list', permanent=False)), 
    path('create/', ArtCreateView.as_view(), name='art_create'),
    path('list/', ArtListView.as_view(), name='art_list'),
    path('update/<int:pk>/', ArtUpdateView.as_view(), name='art_update'),
    path('delete/<int:pk>/', ArtDeleteView.as_view(), name='art_delete'),
]
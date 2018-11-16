from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('image-list/', views.image_list, name='image-list'),
    path('image-search/', views.image_search, name='image-search'),
]

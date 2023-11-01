from django.contrib import admin
from django.urls import path

from .views import index, get_movie, add_new_comment

urlpatterns = [
    path('', index, name='home'),
    path('movie/<int:id>', get_movie, name='get_movie'),
    path('movie/<int:id>/add_new_comment', add_new_comment, name='add_new_comment')
]
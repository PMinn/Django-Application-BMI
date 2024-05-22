from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.members, name='members'),
    path('create_random_members/', views.create_random_members, name='create_random_members'),
    path('new_member/', views.new_member, name='new_member'),
    path('members/delete/', views.delete, name='delete'),
]
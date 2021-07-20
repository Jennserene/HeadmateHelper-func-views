from django.urls import path
from .views import default, new_alter, create_system

urlpatterns = [
    path('', default, name='default'),
    path('new_alter/', new_alter, name='new_alter'),
    path('create_system/', create_system, name='create_system'),
]
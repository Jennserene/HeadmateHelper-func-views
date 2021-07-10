from django.urls import path
from .views import main_chat

urlpatterns = [
    path('', main_chat, name='main_chat'),
]
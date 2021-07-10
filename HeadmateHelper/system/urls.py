from django.urls import path
from .views import new_alter

urlpatterns = [
    # path('', default, name='default'),
    path('new_alter/', new_alter, name='new_alter'),
]
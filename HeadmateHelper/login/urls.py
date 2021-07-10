from django.urls import path
from .views import default, login, signup

urlpatterns = [
    path('', default, name='default'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup')
]
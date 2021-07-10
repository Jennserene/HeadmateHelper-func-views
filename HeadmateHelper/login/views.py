from django.shortcuts import render
from chat.views import main_chat

def default(request):
    if request.user.is_authenticated:
        return redirect('main_chat')
    elif not request.user.is_authenticated:
        return redirect('login')

def login(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass

def signup(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass
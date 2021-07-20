from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Rooms, Chat
from system.models import Headmates, Profile
from system.views import switch





def main_chat(request):
    if len(Rooms.objects.filter(system=request.user.profile, name='main')) == 1:
        current_room = Rooms.objects.filter(system=request.user.profile, name='main')[0]
        room_name = current_room.name

    if request.method == 'GET':
        if len(Headmates.objects.filter(system=request.user.profile, name='Unknown')) == 0: # IF FIRST TIME OPENING APP
            Headmates.objects.create(system=request.user.profile, name='Unknown', front=True)
        chat_history = Chat.objects.filter(room=current_room).order_by('-id')[:100:1]

        context = {
            'room_name': room_name,
            'chat_history': chat_history
        }

        return render(request, 'chat/main.html', context)
    
    if request.method == 'POST':
        if 'chat_send' in request.POST:
            front = Headmates.objects.get(front=True)
            chat_text = request.POST['chat_text']
            Chat.objects.create(room=current_room, headmate=front, text=chat_text)

            return redirect('main_chat')
        elif 'switchFront' in request.POST:
            return switch(request)
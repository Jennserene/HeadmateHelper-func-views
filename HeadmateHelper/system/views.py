from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import FieldError
from django.contrib.auth.models import User
from .models import Headmates, Profile
from chat.models import Rooms
from .forms import NewAlterForm, NewSystemForm

def switch(request):
    if 'switchFront' in request.POST:
        switchVar = request.POST.get('switch', '')
        if switchVar == 'newAlter':
            return redirect(reverse('new_alter'))
        elif switchVar == 'blurry':
            current_front = Headmates.objects.filter(system=request.user.profile, front=True)[0]
            current_front.front = False
            current_front.save()
            new_front = Headmates.objects.filter(system=request.user.profile, name="Unknown")[0]
            new_front.front = True
            new_front.save()
        elif switchVar == 'dropDown':
            current_front = Headmates.objects.filter(system=request.user.profile, front=True)[0]
            current_front.front = False
            current_front.save()
            alter_id = request.POST['switchDropDown']
            new_front = Headmates.objects.get(id=alter_id)
            new_front.front = True
            new_front.save()
        return HttpResponseRedirect(request.path_info)

def new_alter(request):
    if request.method == 'GET':
        form = NewAlterForm()
        context = {
            'form': form
        }
        return render(request, 'system/new_alter.html', context)
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        form = NewAlterForm(request.POST)
        if form.is_valid():
            current_front = Headmates.objects.filter(system=request.user.profile, front=True)[0]
            current_front.front = False
            current_front.save()
            cleaned_name = form.cleaned_data['name']
            cleaned_pronouns = form.cleaned_data['pronouns']
            cleaned_proxy = form.cleaned_data['proxy']
            new_alter = Headmates.objects.create(name=cleaned_name, pronouns=cleaned_pronouns, proxy=cleaned_proxy, front=True)
            
        return HttpResponseRedirect(next)

def create_system(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            form = NewSystemForm()

            context = {
                'form': form
            }

            return render(request, 'system/create_system.html', context)
        else:
            return redirect('account_login')
    if request.method == 'POST':
        form = NewSystemForm(request.POST)
        if form.is_valid():
            sys_name = form.cleaned_data['system_name']
            user = User.objects.get(username=request.user)
            print('user: ', user.id)
            sys = Profile(profile_of=user, system_name=sys_name)
            sys.save()
            Rooms.objects.create(system=sys, name='main')
            Headmates.objects.create(system=sys, name='Unknown', front=True)

def default(request):
    if request.user.is_authenticated:
        try:
            system = Profile.objects.get(user=request.user)
            return redirect('main_chat')
        except(FieldError):
            return redirect('create_system')
    elif not request.user.is_authenticated:
        return redirect('account_login')
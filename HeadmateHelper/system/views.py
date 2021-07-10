from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Headmates
from .forms import NewAlterForm

def switch(request):
    if 'switchFront' in request.POST:
        switchVar = request.POST.get('switch', '')
        if switchVar == 'newAlter':
            return redirect(reverse('new_alter'))
        elif switchVar == 'blurry':
            current_front = Headmates.objects.get(front=True)
            print('current: ', current_front)
            current_front.front = False
            current_front.save()
            new_front = Headmates.objects.get(id=1)
            print('new:', new_front)
            new_front.front = True
            new_front.save()
        elif switchVar == 'dropDown':
            current_front = Headmates.objects.get(front=True)
            print('current', current_front)
            current_front.front = False
            current_front.save()
            alter_id = request.POST['switchDropDown']
            new_front = Headmates.objects.get(id=alter_id)
            print('new', new_front)
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
            current_front = Headmates.objects.get(front=True)
            current_front.front = False
            current_front.save()
            cleaned_name = form.cleaned_data['name']
            cleaned_pronouns = form.cleaned_data['pronouns']
            cleaned_proxy = form.cleaned_data['proxy']
            new_alter = Headmates.objects.create(name=cleaned_name, pronouns=cleaned_pronouns, proxy=cleaned_proxy, front=True)
            
        return HttpResponseRedirect(next)
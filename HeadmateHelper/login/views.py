from django.shortcuts import render, redirect
# from django.contrib.auth.views import LoginView, LogoutView
# from django.views.generic import CreateView
# from django.contrib.auth.forms import UserCreationForm
from chat.views import main_chat
from system.models import Profile, Headmates
from chat.models import Rooms
from .forms import NewSystemForm

def default(request):
    if request.user.is_authenticated:
        system = Profile.objects.get(user=request.user)
        if len(system.headmates.all()) > 0:
            return redirect('main_chat')
        else:
            return redirect('create_system')
    elif not request.user.is_authenticated:
        return redirect('account_login')

def create_system(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            form = NewSystemForm()

            context = {
                'form': form
            }

            return render(request, 'login/create_system.html', context)
        else:
            return redirect('account_login')
    if request.method == 'POST':
        form = NewSystemForm(request.POST)
        if form.is_valid():
            sys_name = form.cleaned_data['system_name']
            sys = System.objects.create(user=request.user, system_name=sys_name)
            Rooms.objects.create(system=sys, name='main')
            Headmates.objects.create(system=sys, name='Unknown', front=True)

# class SystemLoginView(LoginView):
#     template_name = "login/login.html"

# class SystemSignUp(CreateView):
#     model = User
#     form_class = UserCreationForm
#     template_name = 'login/signup.html'
#     success_url = '/login/login/'
from system.models import Headmates
from django.db.models import Q

def header_info(request):
    try:
        front_object = Headmates.objects.filter(system=request.user.profile, front=True)[0]
        front = front_object.name

        headmates_list_raw = Headmates.objects.filter(system=request.user.profile)
        headmates_list = headmates_list_raw.filter(~Q(front=True), ~Q(name='Unknown'))
    except AttributeError:
        front = 'None'
        headmates_list = []

    context = {
        'front': front,
        'headmates_list': headmates_list
    }

    return context
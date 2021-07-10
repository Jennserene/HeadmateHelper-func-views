from system.models import Headmates
from django.db.models import Q

def header_info(request):
    front_object = Headmates.objects.get(front=True)
    front = front_object.name

    headmates_list = Headmates.objects.filter(~Q(id=1), ~Q(front=True))
    print(headmates_list)

    context = {
        'front': front,
        'headmates_list': headmates_list
    }

    return context
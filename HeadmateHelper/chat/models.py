from django.db import models
from system.models import Headmates

class Rooms(models.Model):
    name = models.CharField(max_length=100)

class Chat(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE, related_name='chats')
    headmate = models.ForeignKey(Headmates, on_delete=models.CASCADE, related_name='chats')
    time_stamp = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=2000)
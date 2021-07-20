from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_of = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    system_name = models.CharField(max_length=50, blank=True, null=True)
    public_name = models.CharField(max_length=50, blank=True, null=True)
    body_age = models.IntegerField(blank=True, null=True)
    phone_num = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    medical_info = models.TextField(blank=True, null=True)
    hobbies_interests = models.TextField(blank=True, null=True)

class Headmates(models.Model):
    system = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='headmates')
    name = models.CharField(max_length=50)
    front = models.BooleanField(default=False)
    pronouns = models.CharField(max_length=100, blank=True, null=True)
    host = models.BooleanField(default=False)
    # avatar = models.ImageField(blank=True)
    age = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    age_increments = models.BooleanField(default=False)
    age_slide = models.BooleanField(default=False)
    arrival_day = models.DateField(blank=True, null=True)
    proxy = models.CharField(max_length=20, blank=True, null=True)
    species = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    sexuality = models.CharField(max_length=50, blank=True, null=True)
    roles = models.CharField(max_length=100, blank=True, null=True)
    tells = models.CharField(max_length=100, blank=True, null=True)
    triggers = models.CharField(max_length=200, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    fusion_of = models.CharField(max_length=200, blank=True, null=True)
    appearance = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"name: {self.name}, front: {self.front}"
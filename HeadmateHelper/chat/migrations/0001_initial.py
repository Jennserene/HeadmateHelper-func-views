# Generated by Django 3.2.5 on 2021-07-16 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='system.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=2000)),
                ('headmate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='system.headmates')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='chat.rooms')),
            ],
        ),
    ]

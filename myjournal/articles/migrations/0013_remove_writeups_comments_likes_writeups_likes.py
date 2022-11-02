# Generated by Django 4.1.2 on 2022-10-27 21:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0012_writeups_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writeups_comments',
            name='likes',
        ),
        migrations.AddField(
            model_name='writeups',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='writeupsLikes', to=settings.AUTH_USER_MODEL),
        ),
    ]

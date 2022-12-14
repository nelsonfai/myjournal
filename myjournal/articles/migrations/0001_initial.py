# Generated by Django 4.1.2 on 2022-10-21 13:37

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_alter_mynetwork_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tagline', models.CharField(blank=True, max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='accounts.profile')),
                ('likes', models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.articles')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='userfrofile', to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annoucement', models.CharField(blank=True, max_length=100, null=True)),
                ('annoucement_type', models.CharField(choices=[('I have', 'I have'), ('I need', 'I need'), ('Select', 'Select')], default='Select', max_length=10)),
                ('date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='annouce_profile', to='accounts.profile')),
            ],
        ),
    ]

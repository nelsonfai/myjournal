# Generated by Django 4.1.2 on 2022-10-26 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_prompts_writeups_prompts_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prompts',
            name='posts',
        ),
        migrations.AddField(
            model_name='prompts',
            name='posts',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='writeups', to='articles.writeups'),
        ),
    ]

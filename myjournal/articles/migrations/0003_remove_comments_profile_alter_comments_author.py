# Generated by Django 4.1.2 on 2022-10-21 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_mynetwork_user'),
        ('articles', '0002_remove_articles_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='profile',
        ),
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to='accounts.profile'),
        ),
    ]

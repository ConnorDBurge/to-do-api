# Generated by Django 4.0.2 on 2022-02-13 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_todo', '0002_todo_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]

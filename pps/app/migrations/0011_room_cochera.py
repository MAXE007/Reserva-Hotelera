# Generated by Django 5.1.1 on 2024-12-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_room_wifi'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='cochera',
            field=models.CharField(default='Si', max_length=10),
        ),
    ]
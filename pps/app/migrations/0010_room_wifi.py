# Generated by Django 5.1.1 on 2024-12-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_imagen_roomimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='wifi',
            field=models.CharField(default='Si', max_length=2),
        ),
    ]

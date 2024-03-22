# Generated by Django 5.0.3 on 2024-03-22 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrator',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='profile_picture',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(default=741594863, unique=True),
        ),
    ]

# Generated by Django 3.0.8 on 2020-09-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='Place_of_birth',
            field=models.CharField(default='Nadiad', max_length=30),
        ),
        migrations.AddField(
            model_name='user_details',
            name='homecity',
            field=models.CharField(default='Nadiad', max_length=30),
        ),
    ]

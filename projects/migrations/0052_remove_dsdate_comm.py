# Generated by Django 2.1.2 on 2019-01-08 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0051_dsdate_comm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dsdate',
            name='comm',
        ),
    ]

# Generated by Django 2.1.2 on 2019-01-14 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0058_auto_20190114_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='funding_Satge',
            new_name='funding_Stage',
        ),
    ]

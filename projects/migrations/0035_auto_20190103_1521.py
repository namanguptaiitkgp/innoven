# Generated by Django 2.1.2 on 2019-01-03 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0034_auto_20190103_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='funding',
            new_name='funding_Round',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='overall_status',
            new_name='overall_Status',
        ),
    ]

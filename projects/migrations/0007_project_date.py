# Generated by Django 2.1.2 on 2018-12-13 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_projectinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.1.2 on 2019-01-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0037_auto_20190103_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='amount',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]

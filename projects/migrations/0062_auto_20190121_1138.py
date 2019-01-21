# Generated by Django 2.1.2 on 2019-01-21 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0061_auto_20190118_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='project',
            name='past_loans',
            field=models.CharField(blank=True, help_text='If any past loans have been done.', max_length=200),
        ),
    ]

# Generated by Django 2.1.2 on 2019-01-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0059_auto_20190114_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='past_loans',
            field=models.CharField(blank=True, help_text='If any past loans have been done.', max_length=50),
        ),
    ]
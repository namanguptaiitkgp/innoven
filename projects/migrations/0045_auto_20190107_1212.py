# Generated by Django 2.1.2 on 2019-01-07 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0044_auto_20190107_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='investor',
            field=models.ManyToManyField(blank=True, to='projects.Investor'),
        ),
    ]

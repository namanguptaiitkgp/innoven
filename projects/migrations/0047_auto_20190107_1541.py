# Generated by Django 2.1.2 on 2019-01-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0046_auto_20190107_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='member',
            field=models.ManyToManyField(blank=True, to='projects.Member'),
        ),
    ]

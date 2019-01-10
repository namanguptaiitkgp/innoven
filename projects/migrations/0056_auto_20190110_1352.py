# Generated by Django 2.1.2 on 2019-01-10 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0055_project_closure_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pcompanies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('current_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Currents')),
                ('investor', models.ManyToManyField(blank=True, to='projects.Investor')),
            ],
        ),
        migrations.RemoveField(
            model_name='partner',
            name='companies',
        ),
        migrations.AddField(
            model_name='pcompanies',
            name='partner',
            field=models.ManyToManyField(blank=True, to='projects.Partner'),
        ),
    ]

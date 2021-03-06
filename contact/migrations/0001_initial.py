# Generated by Django 2.2.4 on 2019-08-15 05:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=11)),
                ('message', models.TextField()),
                ('department', models.CharField(max_length=50)),
                ('doctor', models.CharField(max_length=50)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('datee', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
            ],
        ),
    ]

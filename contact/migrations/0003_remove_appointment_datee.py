# Generated by Django 2.2.4 on 2019-08-15 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20190815_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='datee',
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-21 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_patients'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patients',
            options={'verbose_name': 'Patient'},
        ),
        migrations.AlterField(
            model_name='patients',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6),
        ),
    ]

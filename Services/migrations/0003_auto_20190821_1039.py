# Generated by Django 2.2.4 on 2019-08-21 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='price',
            field=models.FloatField(help_text='Enter Test Price'),
        ),
        migrations.AlterField(
            model_name='test',
            name='test',
            field=models.CharField(help_text='Enter Test Name', max_length=20),
        ),
    ]

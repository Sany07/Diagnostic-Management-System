# Generated by Django 2.2.4 on 2019-08-21 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_auto_20190821_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='doctor',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='departments.Doctor'),
        ),
    ]
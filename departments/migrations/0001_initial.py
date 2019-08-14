# Generated by Django 2.2.4 on 2019-08-14 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Subtitle', models.CharField(max_length=40)),
                ('Description', models.TextField()),
                ('Image', models.ImageField(upload_to='departments')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Designation', models.CharField(max_length=40)),
                ('Image', models.ImageField(upload_to='doctors')),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.Department')),
            ],
        ),
    ]

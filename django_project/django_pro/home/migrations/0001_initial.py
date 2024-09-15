# Generated by Django 5.0.7 on 2024-08-05 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teachers_name', models.CharField(max_length=100)),
                ('Teachers_profile', models.TextField()),
                ('Teachers_image', models.ImageField(default='SOME STRING', upload_to='Teachers')),
            ],
        ),
        migrations.CreateModel(
            name='Registor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=500)),
                ('student_phone', models.CharField(max_length=500)),
                ('student_email', models.EmailField(max_length=254)),
                ('Registor_date', models.DateField()),
                ('Registor_on', models.DateField(auto_now=True)),
                ('Book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Books_name', models.CharField(max_length=500)),
                ('Books_class', models.CharField(max_length=300)),
                ('Books_Subject', models.CharField(max_length=300)),
                ('Books_Discription', models.CharField(max_length=300)),
                ('Books_Teachers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.teachers')),
            ],
        ),
    ]

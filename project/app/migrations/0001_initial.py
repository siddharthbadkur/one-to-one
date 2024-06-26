# Generated by Django 5.0.3 on 2024-04-04 06:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AadharModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aadhar_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_Name', models.CharField(max_length=50)),
                ('stu_Email', models.EmailField(max_length=254)),
                ('stu_Contact', models.IntegerField()),
                ('Aadhar_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.aadharmodel')),
            ],
        ),
    ]

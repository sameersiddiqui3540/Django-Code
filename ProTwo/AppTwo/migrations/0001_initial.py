# Generated by Django 2.1.5 on 2019-02-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=254)),
                ('Last_Name', models.CharField(max_length=254)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]

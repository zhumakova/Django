# Generated by Django 3.2.3 on 2021-05-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('full_name', models.CharField(max_length=30)),
                ('exp', models.IntegerField(default=0)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-28 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0004_alter_service_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('date_graduate', models.DateField()),
                ('date_expired', models.DateField()),
                ('school', models.CharField(max_length=40)),
                ('photo', models.ImageField(upload_to='')),
                ('status', models.CharField(choices=[('active', 'active'), ('dead', 'dead')], default='active', max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='spa.master'),
        ),
    ]

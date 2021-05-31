# Generated by Django 3.2.3 on 2021-05-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'cash'), ('wallet', 'wallet')], default='cash', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wallet',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

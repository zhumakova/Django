# Generated by Django 3.2.3 on 2021-06-01 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_auto_20210528_1539'),
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='card',
            name='code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='cvv',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('from_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transaction_from', to='user_profile.profile')),
                ('to_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transaction_to', to='user_profile.profile')),
            ],
        ),
    ]

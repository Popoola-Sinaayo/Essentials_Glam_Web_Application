# Generated by Django 3.0.8 on 2020-10-09 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Essential_Glams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail_subscriber',
            name='Email_Subscribers',
            field=models.EmailField(max_length=400),
        ),
    ]

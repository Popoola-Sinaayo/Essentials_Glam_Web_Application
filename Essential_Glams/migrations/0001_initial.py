# Generated by Django 3.0.8 on 2020-10-09 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail_Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_Subscribers', models.CharField(max_length=400)),
            ],
        ),
    ]

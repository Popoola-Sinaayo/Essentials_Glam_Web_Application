# Generated by Django 3.0.8 on 2020-10-09 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Essential_Glams', '0006_blog_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]

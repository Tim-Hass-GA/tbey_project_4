# Generated by Django 2.0.3 on 2018-04-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbeystore', '0005_auto_20180410_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='tbeystore/static/tbeystore/images/products'),
        ),
    ]

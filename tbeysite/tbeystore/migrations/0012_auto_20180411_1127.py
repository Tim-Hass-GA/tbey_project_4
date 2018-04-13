# Generated by Django 2.0.3 on 2018-04-11 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tbeystore', '0011_auto_20180411_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_order',
            name='order',
        ),
        migrations.AddField(
            model_name='product_order',
            name='payment',
            field=models.CharField(default='placeholder', max_length=200),
        ),
        migrations.AddField(
            model_name='product_order',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0.3 on 2018-04-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tbeystore', '0016_auto_20180412_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='123 4th ave', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='zip',
            field=models.CharField(max_length=5),
        ),
    ]
# Generated by Django 2.2.9 on 2020-04-23 04:31

import bsm_config.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsm_config', '0014_auto_20200422_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='sequence',
            field=models.IntegerField(default=1000, help_text='数值越小，排列越前', verbose_name='排序'),
        ),
    ]

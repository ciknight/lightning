# Generated by Django 2.2.9 on 2020-06-22 07:50

import api_basebone.core.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bsm_config', '0023_setting_help_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='extra_data',
            field=api_basebone.core.fields.JSONField(blank=True, default={}),
        ),
    ]

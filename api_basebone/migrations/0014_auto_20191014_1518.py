# Generated by Django 2.1.3 on 2019-10-14 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basebone', '0013_auto_20191012_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='config',
            field=models.TextField(default='', verbose_name='配置json数据'),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='type',
            field=models.CharField(choices=[('string', '字符串'), ('int', '整数'), ('decimal', '浮点数'), ('boolean', '布尔值'), ('json', 'json格式'), ('PAGE_SIZE', '页长'), ('PAGE_IDX', '页码'), ('pk', '主键')], max_length=20, verbose_name='参数类型'),
        ),
    ]

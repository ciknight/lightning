# Generated by Django 2.2.9 on 2020-08-19 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=201, verbose_name='关联模型')),
                ('groups', models.ManyToManyField(blank=True, help_text='不选会应用于全部', to='auth.Group', verbose_name='关联用户组')),
            ],
            options={
                'verbose_name': '规则',
                'verbose_name_plural': '规则',
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100, verbose_name='字段')),
                ('operator', models.CharField(choices=[('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<='), ('=', '='), ('in', 'in'), ('startswith', 'startswith'), ('endswith', 'endswith'), ('contains', 'contains'), ('icontains', 'icontains'), ('between', 'between'), ('near', 'near'), ('has', 'has'), ('has_any', 'has_any'), ('has_all', 'has_all'), ('isnull', 'isnull')], default='=', max_length=20, verbose_name='操作符')),
                ('variable', models.CharField(choices=[['user', '用户']], default='user', max_length=50, verbose_name='变量')),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shield.Rule', verbose_name='所属规则')),
            ],
            options={
                'verbose_name': '过滤条件',
                'verbose_name_plural': '过滤条件',
            },
        ),
    ]
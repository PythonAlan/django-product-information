# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-22 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0004_auto_20170622_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firstclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=20, verbose_name='国家')),
                ('fee', models.IntegerField(verbose_name='头程¥/kg')),
            ],
            options={
                'verbose_name': '头程设置',
                'verbose_name_plural': '头程设置',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(verbose_name='重量g'),
        ),
    ]
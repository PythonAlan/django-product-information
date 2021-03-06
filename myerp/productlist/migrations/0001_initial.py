# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-21 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='产品目录')),
            ],
            options={
                'verbose_name_plural': '产品目录',
                'verbose_name': '产品目录',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200, verbose_name='产品名称')),
                ('description', models.TextField(verbose_name='产品描述')),
                ('image', models.URLField(verbose_name='产品图片')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='采购价')),
                ('weight', models.IntegerField(verbose_name='重量g')),
                ('volume', models.FloatField(verbose_name='体积m³')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productlist.Category')),
            ],
            options={
                'verbose_name_plural': '产品列表',
                'verbose_name': '产品列表',
                'ordering': ('price',),
            },
        ),
    ]

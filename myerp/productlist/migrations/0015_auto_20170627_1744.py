# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-27 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0014_auto_20170627_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='au_second_cost',
            field=models.FloatField(default=1, verbose_name='澳洲海外小包$'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cn_au_cost',
            field=models.FloatField(default=1, verbose_name='澳洲本地小包$'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cn_de_cost',
            field=models.FloatField(default=1, verbose_name='德国本地小包€'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cn_uk_cost',
            field=models.FloatField(default=1, verbose_name='英国本地小包£'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cn_us_cost',
            field=models.FloatField(default=1, verbose_name='美国本地小包$'),
        ),
        migrations.AlterField(
            model_name='product',
            name='de_second_cost',
            field=models.FloatField(default=1, verbose_name='德国海外小包€'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uk_second_cost',
            field=models.FloatField(default=1, verbose_name='英国海外小包£'),
        ),
        migrations.AlterField(
            model_name='product',
            name='us_second_cost',
            field=models.FloatField(default=1, verbose_name='美国海外小包$'),
        ),
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.FloatField(default=0.001, verbose_name='体积m³'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]

# Generated by Django 2.0.13 on 2019-06-27 09:28

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190619_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column',
            old_name='insto',
            new_name='intro',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='column',
            field=models.ManyToManyField(to='news.Column', verbose_name='归属栏目'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='column',
            name='slug',
            field=models.CharField(db_index=True, max_length=256, verbose_name='栏目网址'),
        ),
    ]

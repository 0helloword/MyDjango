# Generated by Django 2.0.13 on 2019-06-03 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_stauts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='stauts',
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.IntegerField(default='0', verbose_name='状态，1：发布，0：草稿'),
        ),
    ]

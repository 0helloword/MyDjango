# Generated by Django 2.0.13 on 2019-06-03 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='stauts',
            field=models.IntegerField(default='0', verbose_name='状态，1：发布，2：草稿'),
        ),
    ]
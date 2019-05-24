# Generated by Django 2.0.13 on 2019-05-23 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('pub_house', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='data published')),
            ],
        ),
    ]
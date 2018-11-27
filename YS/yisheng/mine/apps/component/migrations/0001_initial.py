# Generated by Django 2.1.2 on 2018-11-22 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, verbose_name='组件名')),
                ('code', models.CharField(default=None, max_length=255, verbose_name='编码')),
                ('path', models.CharField(default=None, max_length=255, verbose_name='路径')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
            ],
        ),
    ]

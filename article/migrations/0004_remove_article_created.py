# Generated by Django 2.2.7 on 2019-11-29 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20191129_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='created',
        ),
    ]

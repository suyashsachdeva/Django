# Generated by Django 3.2.3 on 2021-07-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuckoff', '0002_auto_20210720_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuckoff',
            name='feature',
            field=models.BooleanField(default=False),
        ),
    ]
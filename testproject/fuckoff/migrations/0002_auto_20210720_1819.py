# Generated by Django 3.2.3 on 2021-07-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuckoff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuckoff',
            name='feature',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='fuckoff',
            name='summary',
            field=models.TextField(),
        ),
    ]

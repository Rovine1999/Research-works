# Generated by Django 3.1.7 on 2021-05-27 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210527_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='time_zone',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 3.1.7 on 2021-05-28 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinewriting', '0003_auto_20210529_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]

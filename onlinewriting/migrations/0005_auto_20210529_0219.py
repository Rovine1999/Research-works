# Generated by Django 3.1.7 on 2021-05-28 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinewriting', '0004_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

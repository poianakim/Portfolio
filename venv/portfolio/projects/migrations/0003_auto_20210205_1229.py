# Generated by Django 3.1.6 on 2021-02-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210205_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(default=False, upload_to='images'),
        ),
    ]

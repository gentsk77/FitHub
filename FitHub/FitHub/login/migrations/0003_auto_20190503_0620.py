# Generated by Django 2.0.13 on 2019-05-03 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190503_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='classes',
            field=models.ManyToManyField(blank=True, null=True, to='login.Class'),
        ),
    ]

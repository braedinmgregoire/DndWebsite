# Generated by Django 3.1.6 on 2021-05-04 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20210504_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactermodel',
            name='intelligence',
            field=models.IntegerField(default=13),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='wisdom',
            field=models.IntegerField(default=2),
        ),
    ]
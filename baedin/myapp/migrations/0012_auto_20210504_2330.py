# Generated by Django 3.1.6 on 2021-05-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20210504_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactermodel',
            name='charisma',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='dexterity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='intelligence',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='strength',
            field=models.IntegerField(default=19),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='wisdom',
            field=models.IntegerField(default=9),
        ),
    ]

# Generated by Django 3.1.6 on 2021-04-21 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_auto_20210421_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactermodel',
            name='charisma',
            field=models.IntegerField(default=9),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='dexterity',
            field=models.IntegerField(default=13),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='intelligence',
            field=models.IntegerField(default=14),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='strength',
            field=models.IntegerField(default=8),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='wisdom',
            field=models.IntegerField(default=20),
        ),
    ]

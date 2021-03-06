# Generated by Django 3.1.6 on 2021-04-21 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactermodel',
            name='id',
            field=models.AutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='charisma',
            field=models.IntegerField(default=13),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='dexterity',
            field=models.IntegerField(default=18),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='intelligence',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='player_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='strength',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='charactermodel',
            name='wisdom',
            field=models.IntegerField(default=3),
        ),
    ]

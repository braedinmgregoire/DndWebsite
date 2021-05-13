# Generated by Django 3.1.6 on 2021-04-21 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterModel',
            fields=[
                ('name', models.CharField(max_length=64)),
                ('player_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, serialize=False, to='auth.user')),
                ('description', models.CharField(max_length=256)),
                ('race', models.CharField(default='Human', max_length=24)),
                ('weapon', models.CharField(default='Fists', max_length=32)),
                ('strength', models.IntegerField(default=17)),
                ('dexterity', models.IntegerField(default=7)),
                ('wisdom', models.IntegerField(default=2)),
                ('intelligence', models.IntegerField(default=19)),
                ('charisma', models.IntegerField(default=7)),
            ],
        ),
    ]

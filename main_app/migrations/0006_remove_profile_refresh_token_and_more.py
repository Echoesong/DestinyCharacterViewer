# Generated by Django 4.2 on 2023-04-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_armor_id_alter_weapon_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='refresh_token',
        ),
        migrations.AlterField(
            model_name='profile',
            name='access_token',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='membership_id',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='token_type',
            field=models.CharField(max_length=500),
        ),
    ]

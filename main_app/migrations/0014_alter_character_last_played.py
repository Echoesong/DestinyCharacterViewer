# Generated by Django 4.2 on 2023-04-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_remove_profile_refresh_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='last_played',
            field=models.CharField(max_length=500),
        ),
    ]
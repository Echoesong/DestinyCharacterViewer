# Generated by Django 4.2 on 2023-04-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_profile_refresh_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='destiny2_membership_id',
            field=models.CharField(default='pizzapie', max_length=500),
            preserve_default=False,
        ),
    ]

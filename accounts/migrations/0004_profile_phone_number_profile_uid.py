# Generated by Django 4.1.2 on 2022-10-24 18:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default=1, max_length=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-09 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_alter_address_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='payment_option',
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_orders_coupen_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='variation_id',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-10 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_products_product_img4'),
        ('accounts', '0015_remove_address_payment_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wished_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.products')),
            ],
        ),
    ]

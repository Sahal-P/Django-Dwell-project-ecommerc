# Generated by Django 4.1.3 on 2022-12-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_banner_banner_id_banner_banner_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='selected',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='validity_upto',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='wise',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

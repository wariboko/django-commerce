# Generated by Django 3.2 on 2021-04-13 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210412_0539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='product_id',
            new_name='product_key',
        ),
    ]

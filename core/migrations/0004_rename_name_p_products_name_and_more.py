# Generated by Django 5.0.7 on 2024-07-18 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_nome_products_name_p_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='name_p',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='price_p',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='stock_p',
            new_name='stock',
        ),
    ]
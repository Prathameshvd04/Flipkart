# Generated by Django 5.2 on 2025-04-20 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics', '0003_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='postimages/'),
        ),
    ]

# Generated by Django 3.0.3 on 2020-04-15 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_person_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='product_image',
            field=models.ImageField(default='', upload_to='shop/images/'),
        ),
    ]
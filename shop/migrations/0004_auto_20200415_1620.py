# Generated by Django 3.0.3 on 2020-04-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200415_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='product_image',
            field=models.ImageField(default=' ', upload_to='shop/images'),
        ),
    ]
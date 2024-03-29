# Generated by Django 3.2.18 on 2023-04-26 02:48

import Vision_IMS.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0092_auto_20230419_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='order_currency',
            field=models.CharField(blank=True, help_text='Currency for this order (leave blank to use company default)', max_length=3, null=True, validators=[Vision_IMS.validators.validate_currency_code], verbose_name='Order Currency'),
        ),
        migrations.AddField(
            model_name='returnorder',
            name='order_currency',
            field=models.CharField(blank=True, help_text='Currency for this order (leave blank to use company default)', max_length=3, null=True, validators=[Vision_IMS.validators.validate_currency_code], verbose_name='Order Currency'),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='order_currency',
            field=models.CharField(blank=True, help_text='Currency for this order (leave blank to use company default)', max_length=3, null=True, validators=[Vision_IMS.validators.validate_currency_code], verbose_name='Order Currency'),
        ),
    ]

# Generated by Django 2.2.10 on 2020-03-31 10:00

import Vision_IMS.fields
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_purchaseorderattachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorderlineitem',
            name='quantity',
            field=Vision_IMS.fields.RoundingDecimalField(decimal_places=5, default=1, help_text='Item quantity', max_digits=15, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]

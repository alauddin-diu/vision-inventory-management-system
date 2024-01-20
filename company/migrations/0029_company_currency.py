# Generated by Django 3.0.7 on 2020-11-11 23:22

import Vision_IMS.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0028_remove_supplierpricebreak_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='currency',
            field=models.CharField(blank=True, help_text='Default currency used for this company', max_length=3, validators=[Vision_IMS.validators.validate_currency_code], verbose_name='Currency'),
        ),
    ]
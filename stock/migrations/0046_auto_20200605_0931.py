# Generated by Django 3.0.5 on 2020-06-05 09:31

import Vision_IMS.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0045_stockitem_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklocation',
            name='description',
            field=models.CharField(blank=True, help_text='Description', max_length=250),
        ),
        migrations.AlterField(
            model_name='stocklocation',
            name='name',
            field=models.CharField(help_text='Name', max_length=100, validators=[Vision_IMS.validators.validate_tree_name]),
        ),
    ]

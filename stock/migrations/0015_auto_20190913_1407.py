# Generated by Django 2.2.5 on 2019-09-13 14:07

import Vision_IMS.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0014_auto_20190908_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='URL',
            field=Vision_IMS.fields.Vision_IMSURLField(blank=True, max_length=125),
        ),
        migrations.AlterField(
            model_name='stockitemtracking',
            name='URL',
            field=Vision_IMS.fields.Vision_IMSURLField(blank=True, help_text='Link to external page for further information'),
        ),
    ]

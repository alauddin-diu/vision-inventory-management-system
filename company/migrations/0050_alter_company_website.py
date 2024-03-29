# Generated by Django 3.2.16 on 2022-11-10 01:08

import Vision_IMS.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0049_company_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='website',
            field=Vision_IMS.fields.Vision_IMSURLField(blank=True, help_text='Company website URL', verbose_name='Website'),
        ),
    ]

# Generated by Django 3.2.18 on 2023-04-19 00:37

import Vision_IMS.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0090_auto_20230412_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='notes',
            field=Vision_IMS.fields.Vision_IMSNotesField(blank=True, help_text='Markdown notes (optional)', max_length=50000, null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='returnorder',
            name='notes',
            field=Vision_IMS.fields.Vision_IMSNotesField(blank=True, help_text='Markdown notes (optional)', max_length=50000, null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='notes',
            field=Vision_IMS.fields.Vision_IMSNotesField(blank=True, help_text='Markdown notes (optional)', max_length=50000, null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='salesordershipment',
            name='notes',
            field=Vision_IMS.fields.Vision_IMSNotesField(blank=True, help_text='Markdown notes (optional)', max_length=50000, null=True, verbose_name='Notes'),
        ),
    ]

# Generated by Django 3.2.5 on 2021-11-28 01:51

import Vision_IMS.fields
import Vision_IMS.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0069_auto_20211109_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitemattachment',
            name='link',
            field=Vision_IMS.fields.Vision_IMSURLField(blank=True, help_text='Link to external URL', null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='stockitemattachment',
            name='attachment',
            field=models.FileField(blank=True, help_text='Select file to attach', null=True, upload_to=Vision_IMS.models.rename_attachment, verbose_name='Attachment'),
        ),
    ]

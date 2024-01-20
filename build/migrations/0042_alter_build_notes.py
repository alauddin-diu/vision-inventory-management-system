# Generated by Django 3.2.18 on 2023-04-19 00:37

import Vision_IMS.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0041_alter_build_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='notes',
            field=Vision_IMS.fields.Vision_IMSNotesField(blank=True, help_text='Markdown notes (optional)', max_length=50000, null=True, verbose_name='Notes'),
        ),
    ]
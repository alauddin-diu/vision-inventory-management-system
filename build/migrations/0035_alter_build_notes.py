# Generated by Django 3.2.13 on 2022-06-20 07:28

import Vision_IMS.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0034_alter_build_reference_int'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='notes',
            field=Vision_IMS.fields.Vision_IMSNotesField(blank=True, help_text='Extra build notes', max_length=50000, null=True, verbose_name='Notes'),
        ),
    ]

# Generated by Django 3.2.18 on 2023-05-02 19:56

import Vision_IMS.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0062_contact_metadata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title describing the address entry', max_length=100, verbose_name='Address title')),
                ('primary', models.BooleanField(default=False, help_text='Set as primary address', verbose_name='Primary address')),
                ('line1', models.CharField(blank=True, help_text='Address line 1', max_length=50, verbose_name='Line 1')),
                ('line2', models.CharField(blank=True, help_text='Address line 2', max_length=50, verbose_name='Line 2')),
                ('postal_code', models.CharField(blank=True, help_text='Postal code', max_length=10, verbose_name='Postal code')),
                ('postal_city', models.CharField(blank=True, help_text='Postal code city', max_length=50, verbose_name='City')),
                ('province', models.CharField(blank=True, help_text='State or province', max_length=50, verbose_name='State/Province')),
                ('country', models.CharField(blank=True, help_text='Address country', max_length=50, verbose_name='Country')),
                ('shipping_notes', models.CharField(blank=True, help_text='Notes for shipping courier', max_length=100, verbose_name='Courier shipping notes')),
                ('internal_shipping_notes', models.CharField(blank=True, help_text='Shipping notes for internal use', max_length=100, verbose_name='Internal shipping notes')),
                ('link', Vision_IMS.fields.Vision_IMSURLField(blank=True, help_text='Link to address information (external)', verbose_name='Link')),
                ('company', models.ForeignKey(help_text='Select company', on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='company.company', verbose_name='Company')),
            ],
        ),
    ]

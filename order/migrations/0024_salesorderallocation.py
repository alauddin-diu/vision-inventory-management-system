# Generated by Django 3.0.5 on 2020-04-22 02:09

import Vision_IMS.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0030_auto_20200422_0015'),
        ('order', '0023_auto_20200420_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrderAllocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', Vision_IMS.fields.RoundingDecimalField(decimal_places=5, default=1, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sales_order_allocation', to='stock.StockItem')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allocations', to='order.SalesOrderLineItem')),
            ],
        ),
    ]

# Generated by Django 3.2.18 on 2023-03-14 01:12

import hashlib
import logging

from django.db import migrations
from jinja2 import Template

from Vision_IMS.helpers import normalize


logger = logging.getLogger('Vision_IMS')


def update_bom_item(apps, schema_editor):
    """Update all existing BomItem instances, and cache the 'validated' field.

    The 'validated' field denotes whether this individual BomItem has been validated,
    which previously was calculated on the fly (which was very expensive).
    """

    BomItem = apps.get_model('part', 'bomitem')
    Vision_IMSSetting = apps.get_model('common', 'Vision_IMSsetting')

    n = BomItem.objects.count()

    if n > 0:

        for item in BomItem.objects.all():
            """For each item, we need to re-calculate the "checksum", based on the *old* routine.
            Note that as we cannot access the ORM models, we have to do this "by hand"
            """

            # Construct the 'full_name' for the sub_part (this is no longer required, but *was* required at point of migration)
            try:
                setting = Vision_IMSSetting.objects.get(key='PART_NAME_FORMAT')
                full_name_pattern = str(setting.value)
            except Exception:
                full_name_pattern = "{{ part.IPN if part.IPN }}{{ ' | ' if part.IPN }}{{ part.name }}{{ ' | ' if part.revision }}{{ part.revision if part.revision }}"

            template = Template(full_name_pattern)

            full_name = template.render({'part': item.sub_part})

            # Calculate the OLD checksum manually for this BomItem
            old_hash = hashlib.md5(str(item.pk).encode())
            old_hash.update(str(item.sub_part.pk).encode())
            old_hash.update(str(full_name).encode())
            old_hash.update(str(item.quantity).encode())
            old_hash.update(str(item.note).encode())
            old_hash.update(str(item.reference).encode())
            old_hash.update(str(item.optional).encode())
            old_hash.update(str(item.inherited).encode())

            if item.consumable:
                old_hash.update(str(item.consumable).encode())

            if item.allow_variants:
                old_hash.update(str(item.allow_variants).encode())

            checksum = str(old_hash.digest())

            # Now, update the 'validated' field based on whether the checksum is 'valid' or not
            item.validated = item.checksum == checksum

            """Next, we need to update the item with a "new" hash, with the following differences:
            - Uses the PK of the 'part', not the BomItem itself,
            - Does not use the 'full_name' of the linked 'sub_part'
            - Does not use the 'note' field
            """

            if item.validated:

                new_hash = hashlib.md5(''.encode())

                components = [
                    item.part.pk,
                    item.sub_part.pk,
                    normalize(item.quantity),
                    item.reference,
                    item.optional,
                    item.inherited,
                    item.consumable,
                    item.allow_variants
                ]

                for component in components:
                    new_hash.update(str(component).encode())

                item.checksum = str(new_hash.digest())

            item.save()

        logger.info(f"Updated 'validated' flag for {n} BomItem objects")


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0101_bomitem_validated'),
    ]

    operations = [
        migrations.RunPython(
            update_bom_item,
            reverse_code=migrations.RunPython.noop
        )
    ]

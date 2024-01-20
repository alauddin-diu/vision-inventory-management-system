"""DRF API serializers for the 'users' app"""

from django.contrib.auth.models import Group

from rest_framework import serializers

from Vision_IMS.serializers import Vision_IMSModelSerializer

from .models import Owner


class OwnerSerializer(Vision_IMSModelSerializer):
    """Serializer for an "Owner" (either a "user" or a "group")"""

    class Meta:
        """Metaclass defines serializer fields."""
        model = Owner
        fields = [
            'pk',
            'owner_id',
            'name',
            'label',
        ]

    name = serializers.CharField(read_only=True)

    label = serializers.CharField(read_only=True)


class GroupSerializer(Vision_IMSModelSerializer):
    """Serializer for a 'Group'"""

    class Meta:
        """Metaclass defines serializer fields"""

        model = Group
        fields = [
            'pk',
            'name',
        ]

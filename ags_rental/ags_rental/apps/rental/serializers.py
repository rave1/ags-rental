from rest_framework import serializers

from inventory.models import Case, Device
from rental.models import Rental


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = (
            'id', 'name'
        )


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = (
            'id', 'name'
        )


class RentalSerializer(serializers.ModelSerializer):
    cases = CaseSerializer(many=True, read_only=True)
    devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = Rental
        fields = (
            'person', 'created_at', 'cases', 'devices', 'return_date'
        )

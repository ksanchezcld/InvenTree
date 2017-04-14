from rest_framework import serializers

from .models import UniquePart, PartTrackingInfo


class UniquePartSerializer(serializers.ModelSerializer):

    tracking_info = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UniquePart
        fields = ['pk',
                  'part',
                  'revision',
                  'creation_date',
                  'serial',
                  'createdBy',
                  'customer',
                  'status',
                  'tracking_info']


class PartTrackingInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartTrackingInfo
        fields = '__all__'
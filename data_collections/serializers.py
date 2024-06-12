from rest_framework import serializers
from .models import EssentialsOrganizationUpdate, EssentialsOrganizationUpdateHistory


class EssentialsOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EssentialsOrganizationUpdate
        fields = "__all__"


class EssentialsOrganizationUpdateHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EssentialsOrganizationUpdateHistory
        fields = "__all__"

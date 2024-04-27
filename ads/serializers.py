from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Advertisement
from rest_framework.validators import UniqueValidator


# advertisement serializer
class AdvertisementSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.id")
    id = serializers.ReadOnlyField()

    class Meta:
        model = Advertisement
        fields = ["id", "title", "description", "owner", "active"]

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user.profile
        return Advertisement.objects.create(**validated_data)

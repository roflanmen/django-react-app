from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Profile
from rest_framework.validators import UniqueValidator


class RegistrationSerializer(serializers.ModelSerializer):
    confirmed_password = serializers.CharField()
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=Profile.objects.all())])

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "phone", "username", "email", "password", "confirmed_password", "helper"]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirmed_password"]:
            raise ValidationError("Entered passwords mismatched")

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("confirmed_password")
        return Profile.objects.create_user(**validated_data)


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name", "phone", "username", "email", "helper"]

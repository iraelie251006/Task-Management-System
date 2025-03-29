from rest_framework import serializers
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long')
        elif not any(char.isdigit() for char in value):
            raise serializers.ValidationError('Password must contain at least one digit')
        elif not any(char.isalpha() for char in value):
            raise serializers.ValidationError('Password must contain at least one letter')
        elif not any(char.isupper() for char in value):
            raise serializers.ValidationError('Password must contain at least one uppercase letter')
        else:
            return value
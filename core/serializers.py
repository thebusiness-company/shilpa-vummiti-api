from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(
        source='date_of_birth',
        required=False,
        format='%d-%B-%Y',  # Display format: 12-April-2025
        input_formats=['%d-%B-%Y', '%d-%m-%Y', '%Y-%m-%d']  # Acceptable input formats
    )

    class Meta:
        model = CustomUser
        fields = [
            'email', 'first_name', 'last_name', 'username', 'is_superuser',
            'phone_number', 'city', 'gender', 'address', 'profile_picture',
            'zip_code', 'dob','country','state'
        ]
        read_only_fields = ['date_joined', 'last_login']
        
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs
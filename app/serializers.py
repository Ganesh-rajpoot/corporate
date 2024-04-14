from .models import User,Mentor,ContactUs
from rest_framework import serializers
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'mobile', 'password', 'referral_code']
        extra_kwargs = {'password': {'write_only': True}}  # Hide password field in GET requests

class LoginSerializer(serializers.Serializer):
    mobile = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        mobile = attrs.get('mobile')
        password = attrs.get('password')

        if mobile and password:
            user = authenticate(mobile=mobile, password=password)
            if user:
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'mobile' and 'password'.")

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ['first_name', 'last_name', 'email_id', 'mobile_number', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}, 'confirm_password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("The passwords do not match.")
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return Mentor.objects.create(**validated_data)

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['name', 'mobile', 'email', 'message']
from rest_framework import serializers
from .models import CustomUser, UserProfile
from dj_rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer class to seralize CustomUser model.
    """


class ProfileSerializer(CustomUserSerializer):
    """
    Serializer class to serialize the user Profile model
    """
    class Meta:
        model = UserProfile
        fields = ('description')


class LoginSerializer(RestAuthLoginSerializer):
    username = None
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')
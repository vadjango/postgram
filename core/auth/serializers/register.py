from rest_framework import serializers

from core.user.models import User
from core.user.serializers import UserSerializer


class RegistrationSerializer(UserSerializer):
    password = serializers.CharField(min_length=8, max_length=128, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'first_name',
                  'last_name',
                  'bio',
                  'avatar',
                  'email',
                  'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

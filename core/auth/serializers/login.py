from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

from core.user.serializers import UserSerializer


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(user=self.user)
        data["user"] = UserSerializer(self.user).data
        data["access"] = str(refresh.access_token)
        data["refresh"] = str(refresh)
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data

import logging

from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from core.auth.serializers.register import RegistrationSerializer


class RegistrationViewSet(viewsets.ViewSet):
    http_method_names = ('post',)
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        reg_serializer = self.serializer_class(data=request.data)
        reg_serializer.is_valid(raise_exception=True)
        user = reg_serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": reg_serializer.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)

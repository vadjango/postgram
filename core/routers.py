from rest_framework import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegistrationViewSet, LoginViewSet, RefreshViewSet
from core.post.viewsets import PostViewSet

router = routers.SimpleRouter()

router.register(r'user', UserViewSet, basename='user')
router.register(r'auth/register', RegistrationViewSet, basename="auth-register")
router.register(r'auth/login', LoginViewSet, basename="auth-login")
router.register(r'auth/refresh', RefreshViewSet, basename="auth-refresh")
router.register(r'post', PostViewSet, basename="post")

urlpatterns = [
    *router.urls
]

from django.urls import path, include
from jwt_passwordless.views import (
    ObtainEmailCallbackToken,
    ObtainAuthTokenFromCallbackToken
)

urlpatterns = [
    # path("", include("jwt_passwordless.urls", namespace="jwt_passwordless")),
    path("auth/request-code/", ObtainEmailCallbackToken.as_view(), name='auth_email'),
    path("auth/verify-code/", ObtainAuthTokenFromCallbackToken.as_view(), name='auth_token')
]

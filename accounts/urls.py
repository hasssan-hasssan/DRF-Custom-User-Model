from django.urls import path
from jwt_passwordless.views import (
    ObtainEmailCallbackToken,
    ObtainAuthTokenFromCallbackToken,
)
from accounts import views

urlpatterns = [
    # path("", include("jwt_passwordless.urls", namespace="jwt_passwordless")),
    path(
        "auth/request-code/",
        ObtainEmailCallbackToken.as_view(),
        name="auth_email",
    ),
    path(
        "auth/verify-code/",
        ObtainAuthTokenFromCallbackToken.as_view(),
        name="auth_token",
    ),
    path(
        "auth/register/", views.PasswordlessRegisterView.as_view(), name="register_user"
    ),
]

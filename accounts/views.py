from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PasswordlessRegisterSerializer


class PasswordlessRegisterView(APIView):
    """
    Registration view for passwordless login using CustomUser.
    If user does not exist, create it.
    Then instruct frontend to request OTP from jwt-passwordless endpoint.
    """

    def post(self, request):
        serializer = PasswordlessRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user, created = serializer.create_or_get_user()

        if created:
            message = "User created successfully. Now request OTP to login."
        else:
            message = "User already exists. Request OTP to login."

        return Response(
            {
                "message": message,
                "is_new_user": created,
                "next_step": "http:/127.0.0.1:8000/api/v1/accounts/auth/request-token/",  # Endpoint from jwt-passwordless
            },
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )

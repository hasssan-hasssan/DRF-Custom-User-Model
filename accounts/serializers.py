from rest_framework import serializers
from accounts.models import CustomUser


class PasswordlessRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    full_name = serializers.CharField(required=False, allow_blank=True)

    def create_or_get_user(self):
        email = self.validated_data["email"]
        full_name = self.validated_data.get("full_name", "")

        user, created = CustomUser.objects.get_or_create(
            email=email,
            defaults={"full_name": full_name, "is_verified": False, "is_active": True},
        )

        return user, created

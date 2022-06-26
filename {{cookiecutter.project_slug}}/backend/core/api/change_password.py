from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password1 = serializers.CharField(
        max_length=128, write_only=True, required=True
    )
    new_password2 = serializers.CharField(
        max_length=128, write_only=True, required=True
    )

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                _("Your old password was entered incorrectly. Please enter it again.")
            )
        return value

    def validate(self, data):
        if data["new_password1"] != data["new_password2"]:
            raise serializers.ValidationError(
                {"new_password2": _("The two password fields didn't match.")}
            )
        password_validation.validate_password(
            data["new_password1"], self.context["request"].user
        )
        return data

    def save(self, **kwargs):
        password = self.validated_data["new_password1"]
        user = self.context["request"].user
        user.set_password(password)
        user.save()
        return user


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # if using drf authtoken, create a new token
        if hasattr(user, "auth_token"):
            user.auth_token.delete()
        token, created = Token.objects.get_or_create(user=user)
        # return new token
        return Response({"token": token.key}, status=status.HTTP_200_OK)

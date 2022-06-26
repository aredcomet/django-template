from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "last_login",
            "is_superuser",
            "username",
            "email",
            "phone_number",
            "is_staff",
            "is_active",
            "date_joined",
            "name",
            "avatar",
        )

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = (
        "id",
        "last_login",
        "is_superuser",
        "username",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
        "name",
    )

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

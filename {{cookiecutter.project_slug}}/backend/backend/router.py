from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter() if settings.DEBUG else SimpleRouter()
from core.api.user import UserViewSet

router.register("user", UserViewSet)

app_name = "rest-api"
urlpatterns = router.urls


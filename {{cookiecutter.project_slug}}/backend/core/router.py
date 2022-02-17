from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("user", UserViewSet)

app_name = "core-api"
urlpatterns = router.urls


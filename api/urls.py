from rest_framework import routers
from api.views import LoginViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"login", LoginViewSet, basename="login")

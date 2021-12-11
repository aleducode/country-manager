from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from country_manager.users.api.views import UserViewSet
from country_manager.countries.api.views import CountryViewSet, GonorreaViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("countries", CountryViewSet)
router.register("gonorrea", GonorreaViewSet)



app_name = "api"
urlpatterns = router.urls

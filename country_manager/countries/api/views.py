"""Countries api views."""

from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from country_manager.countries.models import Country
from country_manager.countries.api.serializers import (
    SerializerCountry,
    SerializerRestrictedCountry,
    BaseSerializerCountry
)
# Filters
from rest_framework.filters import SearchFilter


class CountryViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated]
    queryset = Country.objects.all()
    serializer_class = SerializerCountry
    filter_backends = (SearchFilter,)
    search_fields = ['=phone_prefix']

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'list':
            return SerializerCountry
        else:
            return SerializerRestrictedCountry


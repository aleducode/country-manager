from django.db.models import fields
from rest_framework import serializers
from country_manager.countries.models import Country, Currency


class SerializerCurrency(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ['code']


class BaseSerializerCountry(serializers.ModelSerializer):

    currency = serializers.StringRelatedField(many=False)

    class Meta:
        model = Country
        fields = ('id', 'name', 'flag_icon', 'currency')


class SerializerCountry(BaseSerializerCountry):


    class Meta(BaseSerializerCountry.Meta):
        fields = BaseSerializerCountry.Meta.fields + ('phone_prefix',)


class SerializerRestrictedCountry(serializers.ModelSerializer):
    currency = SerializerCurrency(many=False)

    class Meta:
        model = Country
        fields = ["name", "currency"]

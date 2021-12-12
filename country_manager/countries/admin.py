"""Countries admin."""

from django.contrib import admin
from country_manager.countries.models import Country, Currency


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """Country admin."""
    search_fields = ['name', "phone_prefix"]


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    """Currency admin."""
    pass

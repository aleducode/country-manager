"""Custom Command."""
import requests

# Django
from django.core.management.base import BaseCommand
from country_manager.countries.models import Country, Currency

class Command(BaseCommand):
    """Set massive route."""

    def handle(self, *args, **options):
        """Handle command usage."""
        data = requests.get('https://restcountries.com/v3.1/all')
        if data.status_code == 200:
            raw_data = data.json()
            for country_data in raw_data:
                currencies = country_data.get('currencies')
                currency_name = None
                currency_symbol = None
                name = country_data.get('name').get('official')
                if currencies:
                    for key, values in currencies.items():
                        currency_name = values.get('name')
                        currency_symbol = values.get('symbol')
                        if currency_name and currency_symbol:
                            break
                    currency, _ = Currency.objects.get_or_create(
                        name=currency_name,
                        code=currency_symbol
                    )
                else:
                    print(f"Oe que gonorrea de pais sin plata {name}")
                    currency = None
                if currency:
                    phone_dict = country_data.get('idd')
                    final_phone_prefix = "{prefix}{sufix}".format(
                        prefix=phone_dict.get('root'),
                        sufix=phone_dict.get('suffixes')[0] if phone_dict.get('suffixes') else ''
                    )
                    country, _ = Country.objects.get_or_create(
                        name=name,
                        phone_prefix=final_phone_prefix,
                        flag_icon=country_data.get('flag'),
                        currency=currency
                    )
                    print(f"Created country with name {name}")

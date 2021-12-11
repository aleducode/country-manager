"""Country models."""

from django.db import models


class Currency(models.Model):
    """Currency model."""

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.code if self.code else "$"

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"


class Country(models.Model):
    """Country model."""
    name = models.CharField(max_length=100)
    phone_prefix = models.CharField(max_length=10)
    flag_icon = models.CharField(max_length=100, blank=True, null=True)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='countries'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

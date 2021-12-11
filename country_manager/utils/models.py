"""Django models utilities."""

# Django
from django.db import models

COUNTRY_CODES = [
    ('+57', '+57'),
    ('+54', '+54'),
    ('+34', '+34'),
    ('+593', '+593'),
    ('+39', '+39'),
    ('+52', '+52'),
    ('+51', ' +51'),
    ('+502', '+502'),
    ('+58', '+58'),
    ('+1', '+1'),
    ('+56', '+56'),

]

CURRENCY_CODES = [
    ('', 'Seleccionar'),
    ('COP', 'Colombian Pesos'),
    ('MX', 'Mexican Pesos'),
    ('USD', 'USA Dollards'),
]


class HackuModel(models.Model):
    """Hacku base model.

    HackuModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created.
        + modified (DateTime): Store the last datetime the object was modified.
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta option."""

        # does not show in db
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']


class MessageModel(HackuModel):
    """Hacku message base model.

    MessageModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + sent (Boolean): Store the datetime the object was created.
        + message (DateTime): Store the last datetime the object was modified.
    """

    sent = models.BooleanField(
        'was sent?',
        default=False,
        help_text='Set true when message is send.'
    )
    date_sent = models.DateField('Date sent', null=True, blank=True)

    text = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        """Meta option."""

        # does not show in db
        abstract = True

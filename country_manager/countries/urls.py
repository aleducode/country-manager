"""Countries URLs."""

# Django
from django.urls import path
from django.views.generic import TemplateView

from country_manager.countries import views as countries_views

# View
app_name = 'countries'
urlpatterns = [
    path(
        route='',
        view=countries_views.IndexView.as_view(),
        name='index'
    ),
]

from django.urls import path

from immobile.views import ImmobileView

urlpatterns = [
    path("", ImmobileView.as_view(), name="immobile"),  # URL without parameter
    path("<int:id>/", ImmobileView.as_view(), name="immobile"),
]

from django.urls import path

from reserve.views import ReserveView

urlpatterns = [
    path("", ReserveView.as_view(), name="reserve"),  # URL without parameter
    path("<int:id>/", ReserveView.as_view(), name="reserve"),
]

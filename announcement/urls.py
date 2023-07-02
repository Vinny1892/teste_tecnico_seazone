from django.urls import path

from announcement.views import AnnouncementView

urlpatterns = [
    path("", AnnouncementView.as_view(), name="announcement"),  # URL without parameter
    path("<int:id>/", AnnouncementView.as_view(), name="announcement"),
]

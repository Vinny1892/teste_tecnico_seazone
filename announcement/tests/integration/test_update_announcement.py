from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from announcement.factories import AnnouncementFactory
from immobile.factories import ImmobileFactory
from immobile.models import Immobile


class TestUpdateAnnouncementIntegration(APITestCase):
    def setUp(self):
        self.announcement = AnnouncementFactory()

    def test_update_announcement_success(self):
        data = {
            "tax_platform": "9.00",
            "name_platform": "Platform A",
            "immobile_id": self.announcement.immobile.id,
        }

        response = self.client.put(
            reverse("announcement", kwargs={"id": self.announcement.id}), data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_announcement_without_exists(self):
        response = self.client.put(reverse("announcement", kwargs={"id": 5}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

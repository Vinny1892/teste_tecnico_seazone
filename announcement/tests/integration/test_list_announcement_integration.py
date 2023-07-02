from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from announcement.factories import AnnouncementFactory
from immobile.factories import ImmobileFactory
from immobile.serializers import ImmobileSerializer


class TestListAnnouncementIntegration(APITestCase):
    def setUp(self):
        self.numberOfAnnouncement = 5
        self.announcement = AnnouncementFactory.create_batch(self.numberOfAnnouncement)

    def test_list_all_announcement_success(self):
        response = self.client.get(reverse("announcement"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.announcement))
        self.assertGreater(len(response.data), 0)

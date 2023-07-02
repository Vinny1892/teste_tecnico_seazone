from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from announcement.factories import AnnouncementFactory
from announcement.serializers import AnnouncementSerializer
from immobile.factories import ImmobileFactory
from immobile.serializers import ImmobileSerializer
from reserve_announcement_immobile.helpers.model_to_dict import (
    model_to_data_input, response_to_data_input)


class TestGetAnnouncementIntegration(APITestCase):
    def setUp(self):
        self.announcement = AnnouncementFactory()
        self.data = model_to_data_input(
            model=self.announcement, serializer=AnnouncementSerializer
        )

    def test_get_announcement_by_id_success(self):
        response = self.client.get(
            reverse("announcement", kwargs={"id": self.announcement.id})
        )
        response_data = response_to_data_input(
            model=self.announcement,
            serializer=AnnouncementSerializer,
            response_data=response.data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, self.data)

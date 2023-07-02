from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from immobile.factories import ImmobileFactory


class TestCreateAnnouncementIntegration(APITestCase):
    def setUp(self):
        self.immobile = ImmobileFactory()

    def test_create_announcement_success(self):
        data = {
            "tax_platform": "10.50",
            "name_platform": "Platform X",
            "immobile_id": self.immobile.id,
        }
        response = self.client.post(reverse("announcement"), data)
        common_keys = set(response.data.keys()) & set(data.keys())
        response_data = {key: response.data[key] for key in common_keys}
        response_data["immobile_id"] = response.data['immobile']['id']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictEqual(response_data, data)

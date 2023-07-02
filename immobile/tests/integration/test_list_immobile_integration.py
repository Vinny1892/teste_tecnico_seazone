from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from immobile.factories import ImmobileFactory
from immobile.serializers import ImmobileSerializer
from reserve_announcement_immobile.helpers.model_to_dict import (
    model_to_data_input, response_to_data_input)


class TestListImmobileIntegration(APITestCase):
    def setUp(self):
        self.numberOfImmobile = 5
        self.immobile = ImmobileFactory.create_batch(self.numberOfImmobile)

    def test_list_all_immobile_success(self):
        response = self.client.get(reverse("immobile"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.immobile))
        self.assertGreater(len(response.data), 0)

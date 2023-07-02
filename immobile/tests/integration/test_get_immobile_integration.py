from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from immobile.factories import ImmobileFactory
from immobile.serializers import ImmobileSerializer
from reserve_announcement_immobile.helpers.model_to_dict import (
    model_to_data_input, response_to_data_input)


class TestGetImmobileIntegration(APITestCase):
    def setUp(self):
        self.immobile = ImmobileFactory()
        self.data = model_to_data_input(
            model=self.immobile, serializer=ImmobileSerializer
        )

    def test_get_immobile_by_id_success(self):
        response = self.client.get(reverse("immobile", kwargs={"id": self.immobile.id}))
        response_data = response_to_data_input(
            model=self.immobile,
            serializer=ImmobileSerializer,
            response_data=response.data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, self.data)

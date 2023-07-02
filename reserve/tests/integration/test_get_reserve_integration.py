from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from reserve.factories import ReserveFactory
from reserve.serializers import ReserveSerializer
from reserve_announcement_immobile.helpers.model_to_dict import (
    model_to_data_input, response_to_data_input)


class TestGetAnnouncementIntegration(APITestCase):
    def setUp(self):
        self.reserve = ReserveFactory()
        self.data = model_to_data_input(
            model=self.reserve, serializer=ReserveSerializer
        )

    def test_get_reserve_by_id_success(self):
        response = self.client.get(reverse("reserve", kwargs={"id": self.reserve.id}))
        response_data = response_to_data_input(
            model=self.reserve,
            serializer=ReserveSerializer,
            response_data=response.data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, self.data)

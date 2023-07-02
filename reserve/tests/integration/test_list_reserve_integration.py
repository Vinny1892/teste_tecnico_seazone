from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from reserve.factories import ReserveFactory


class TestListReserveIntegration(APITestCase):
    def setUp(self):
        self.numberOfReserves = 5
        self.reserve = ReserveFactory.create_batch(self.numberOfReserves)

    def test_list_all_reserves_success(self):
        response = self.client.get(reverse("reserve"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.reserve))
        self.assertGreater(len(response.data), 0)

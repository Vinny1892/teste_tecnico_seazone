from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from immobile.factories import ImmobileFactory
from immobile.models import Immobile
from reserve.factories import ReserveFactory


class TestDeleteReserveIntegration(APITestCase):
    def setUp(self):
        self.reserve = ReserveFactory()

    def test_delete_reserve_success(self):
        response = self.client.delete(
            reverse("reserve", kwargs={"id": self.reserve.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_reserve_without_exists(self):
        response = self.client.delete(reverse("reserve", kwargs={"id": 5}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

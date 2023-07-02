from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from immobile.factories import ImmobileFactory
from immobile.models import Immobile


class TestUpdateImmobileIntegration(APITestCase):
    def setUp(self):
        self.immobile = ImmobileFactory()

    def test_update_immobile_success(self):
        data = {
            "code": self.immobile.code,
            "activation_date": self.immobile.activation_date,
            "accept_pet": True,
            "quantity_toilet": 4,
            "amount_clean": self.immobile.amount_clean,
        }

        response = self.client.put(
            reverse("immobile", kwargs={"id": self.immobile.id}), data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_immobile_without_exists(self):
        response = self.client.put(reverse("immobile", kwargs={"id": 5}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

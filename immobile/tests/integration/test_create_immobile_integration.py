from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from immobile.models import Immobile


class TestCreateImmobileIntegration(APITestCase):
    def test_create_immobile_success(self):
        data = {
            "code": 12354,
            "quantity_toilet": 5,
            "accept_pet": False,
            "activation_date": "2023-06-21T00:00:00Z",
            "amount_clean": "252.50",
        }
        response = self.client.post(reverse("immobile"), data)
        common_keys = set(response.data.keys()) & set(data.keys())
        response_data = {key: response.data[key] for key in common_keys}
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictEqual(response_data, data)

    def test_create_immobile_with_code_already_in_use(self):
        Immobile.objects.create(
            code=12354,
            quantity_toilet=5,
            accept_pet=True,
            activation_date="2023-06-21T00:00:00Z",
            amount_clean=252.50,
        )
        data = {
            "code": 12354,
            "quantity_toilet": 5,
            "accept_pet": False,
            "activation_date": "2023-06-21T00:00:00Z",
            "amount_clean": "252.50",
        }
        response = self.client.post(reverse("immobile"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

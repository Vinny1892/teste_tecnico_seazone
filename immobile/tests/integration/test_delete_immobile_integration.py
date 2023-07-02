from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from immobile.factories import ImmobileFactory
from immobile.models import Immobile


class TestDeleteImmobileIntegration(APITestCase):
    def setUp(self):
        self.immobile = ImmobileFactory()

    def test_delete_immobile_success(self):
        response = self.client.delete(
            reverse("immobile", kwargs={"id": self.immobile.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_immobile_without_exists(self):
        response = self.client.delete(reverse("immobile", kwargs={"id": 5}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

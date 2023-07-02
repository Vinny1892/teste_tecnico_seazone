import datetime


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from announcement.factories import AnnouncementFactory


class TestCreateReserveIntegration(APITestCase):
    def setUp(self):
        self.announcement = AnnouncementFactory()

    def test_create_reserve_success(self):
        data = {
            "quantity_guests": 2,
            "total_price": "99.99",
            "comment": "This is a comment",
            "check_in": "2023-07-01T10:00:00Z",
            "check_out": "2023-07-05T12:00:00Z",
            "announcement_id": self.announcement.id,
        }
        response = self.client.post(reverse("reserve"), data)
        common_keys = set(response.data.keys()) & set(data.keys())
        response_data = {key: response.data[key] for key in common_keys}
        response_data['announcement_id'] = response.data['announcement']['id']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictEqual(response_data, data)


    def test_create_error_with_checkout_date_is_after_checkout_date(self):
        data = {
            "quantity_guests": 2,
            "total_price": "99.99",
            "comment": "This is a comment",
            # "check_in": "2023-07-05T10:00:00Z",
            # "check_out": "2023-07-01T12:00:00Z",
            "check_in": datetime.datetime(2023,7,3).strftime('%Y-%m-%dT%H:%M:%SZ'),
            "check_out":  datetime.datetime(2023,7,1).strftime('%Y-%m-%dT%H:%M:%SZ'),
            "announcement_id": self.announcement.id,
        }
        response = self.client.post(reverse("reserve"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
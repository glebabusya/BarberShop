from collections import OrderedDict

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from employers import models, serializers, servises
from base.models import BarberShop

UserModel = get_user_model()


class EmployeeTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        user_1 = UserModel.objects.create(
            first_name="first name 1", last_name="last name 1", email="test1@gmail.com"
        )
        user_2 = UserModel.objects.create(
            first_name="first name 2", last_name="last name 2", email="test2@gmail.com"
        )

        employee_1 = models.Employee.objects.create(
            user=user_1, phone_number="+48000000000", rating=4.2, is_available=False
        )
        employee_2 = models.Employee.objects.create(
            user=user_2, phone_number="+48111111111", rating=5.0
        )

    def test_employee_list_ok(self):
        expected_data = OrderedDict(
            [
                ("first_name", "first name 2"),
                ("last_name", "last name 2"),
                ("email", "test2@gmail.com"),
                ("phone_number", "+48111111111"),
                ("photo", None),
                ("rating", "5.0"),
                ("barbershop", None),
            ]
        )

        url = reverse("employee-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0], expected_data)

    def test_employee_create(self):
        url = reverse("employee-list")
        response = self.client.post(
            url,
            data={
                "first_name": "first name  3",
                "last_name": "last name 3",
                "email": "test3@gmail.com",
                "password": "test_password",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Employee.objects.all().count(), 3)

    def test_employee_password_set_ok(self):
        url = reverse("employee-set-password", args=(2, ))
        response = self.client.post(
            url, data={
                "password": "test",
                "password2": "test"
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": "password set"})

    def test_employee_password_set_400(self):
        url = reverse("employee-set-password", args=(2, ))
        response = self.client.post(
            url, data={
                "password": "test",
                "password2": "test2"
            }
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["non_field_errors"][0], "Passwords do not match")

from django.shortcuts import reverse
from rest_framework.test import APITestCase
from employees import views

def test_employee_list(self):
        response = client.post(
            reverse('employee_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


def test_employees_detail(self):
        response = client.post(
            reverse('employees_detail'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

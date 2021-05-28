from django.test import TestCase
from django.urls import reverse

from .models import Service,Master

class ServiceTest(TestCase):
    def setUp(self):
        self.url=reverse('services')
        self.master=Master.objects.create(full_name='maksim',exp=2,birth_date="2021-05-05")
        Service.objects.create(name='zagar',price=700,master=self.master)

    def test_service_get(self):
        self.response=self.client.get(self.url)
        self.assertEqual(self.response.status_code,200)

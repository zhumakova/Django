
from django.urls import reverse
from django.test import TestCase
from .models import User,Profile


class SimpleTestCase:
    pass


class RegisterTest(TestCase):

    def setUp(self)->None:
        self.url=reverse('register')


    def test_register_ok(self):
        data={
            'name':'maksim',
            'age':22,
            'email':'maxim@gmail.com',
            'username':'maksim1',
            'password1':"django321",
            'password2':"django321",
        }
        self.response=self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,200)

    def test_register_bad_email(self):
        data={
            'name': 'maksim',
            'age': 22,
            'username': 'maksim1',
            'password1': "django321",
            'password2': "django321",
        }
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response,field='email',errors='This field is required.',form='form')

    def test_register_bad_username(self):
        data={
            'name': 'maksim',
            'age': 22,
            'email': 'maxim@gmail.com',
            'password1': "django321",
            'password2': "django321",
        }
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response,field='username',errors='This field is required.',form='form')

    def test_register_bad_password1(self):
        data={
            'name': 'maksim',
            'age': 22,
            'email': 'maxim@gmail.com',
            'username': 'maksim1',
            'password2': "django321",
        }
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response,field='password1',errors='This field is required.',form='form')

    def test_register_bad_password2(self):
        data = {
            'name': 'maksim',
            'age': 22,
            'email': 'maxim@gmail.com',
            'username': 'maksim1',
            'password1': "django321",
        }
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response, field='password2', errors='This field is required.', form='form')

    def test_register_bad_name(self):
        data = {
            'age': 22,
            'email': 'maxim@gmail.com',
            'username': 'maksim1',
            'password1': "django321",
            'password2': "django321",
        }
        self.response = self.client.post(self.url, data)
        self.assertFormError(self.response, field='name', errors='This field is required.', form='form')
        self.assertTemplateUsed(self.response,'register.html',count=None)

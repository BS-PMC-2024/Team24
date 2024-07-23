from django.test import SimpleTestCase
from django.urls import reverse, resolve
# from django.contrib import admin
from ReqGenius.views import HomePage, signup, Login

class UrlTests(SimpleTestCase):
    #     url = reverse('admin:index') test!

    def test_home_url_resolves_home_page_view(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, HomePage)

   

    def test_signup_url_resolves_signup_view(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signup)

    def test_login_url_resolves_login_view(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, Login)
from django.test import TestCase, Client
from django.urls import reverse

class HomeViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'Home.html')



class SignupViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_view_status_code(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html')

class LoginViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_view_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'Login.html')

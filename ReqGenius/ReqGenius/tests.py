from django.test import TestCase
from django.urls import reverse
from django.test import TestCase

class SimpleTest(TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)


class ViewsTestCase(TestCase):

    def test_home_page_view(self):
        response = self.client.get(reverse('HomePage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Home.html')

    # def test_about_view(self):
    #     response = self.client.get(reverse('about'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'about.html')

    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_login_view(self):
        response = self.client.get(reverse('Login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Login.html')

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users import views

class UrlTests(SimpleTestCase):

    def test_home_url_resolves_home_view(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, views.home)

    def test_signup_url_resolves_signup_view(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, views.signup)

    def test_login_url_resolves_login_view(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, views.login)

    def test_support_url_resolves_support_view(self):
        url = reverse('support')
        self.assertEqual(resolve(url).func, views.support)

    def test_feedback_url_resolves_feedback_view(self):
        url = reverse('feedback')
        self.assertEqual(resolve(url).func, views.feedback)

    def test_feedback_html_url_resolves_feedback_view(self):
        url = reverse('feedback_html')
        self.assertEqual(resolve(url).func, views.feedback)

    def test_srsinfo_url_resolves_srsinfo_view(self):
        url = reverse('srsinfo')
        self.assertEqual(resolve(url).func, views.srsinfo)

    def test_srsinfo_html_url_resolves_srsinfo_view(self):
        url = reverse('srsinfo_html')
        self.assertEqual(resolve(url).func, views.srsinfo)

    def test_err_url_resolves_err_view(self):
        url = reverse('err')
        self.assertEqual(resolve(url).func, views.err)

    def test_err_html_url_resolves_err_view(self):
        url = reverse('err_html')
        self.assertEqual(resolve(url).func, views.err)

    def test_srs_url_resolves_srs_view(self):
        url = reverse('srs')
        self.assertEqual(resolve(url).func, views.srs)

    def test_about_url_resolves_about_view(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, views.about)

    def test_dash_student_url_resolves_dash_student_view(self):
        url = reverse('dashStudent')
        self.assertEqual(resolve(url).func, views.dashStudent)

    def test_dash_client_url_resolves_dash_client_view(self):
        url = reverse('dashClient')
        self.assertEqual(resolve(url).func, views.dashClient)

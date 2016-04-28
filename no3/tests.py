from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from no3.views import login_page


# Create your tests here.

class LoginPageTest(TestCase):

    def test_root_url_resolves_to_login_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, login_page)


    def test_login_page_returns_correct_html(self):
        request = HttpRequest()
        response = login_page(request)
        expected_html = render_to_string('login.html')
        self.assertEqual(response.content.decode(), expected_html)

from django.core.urlresolvers import resolve
from django.test import TestCase
from no3.views import login_page


# Create your tests here.

class LoginPageTest(TestCase):

    def test_root_url_resolves_to_login_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, login_page)

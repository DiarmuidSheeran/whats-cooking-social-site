from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import *

class TestUrls(SimpleTestCase):

    def test_landing_url_is_resolved(self):
        url = reverse('landing')
        resolved = resolve(url)
        self.assertEqual(resolved.func, landing)
        self.assertNotEqual(resolved.func, unauthenticated_user)

    
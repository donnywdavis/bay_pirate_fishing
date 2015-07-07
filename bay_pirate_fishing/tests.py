from django.core.urlresolvers import reverse
from django.test import TestCase


class StaticViewTests(TestCase):

    def test_home_page_exists(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_exists(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

from django.urls import resolve
from django.test import TestCase
from blog.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):  # проверяет, что при попытке открытия страницы у Django вызывется нужная view(home_page)
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):  # view(home_page) открывает правильный html
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Рецепты</title>', html)
        # self.assertIn('logo.png', html)
        self.assertTrue(html.endswith('</html>'))





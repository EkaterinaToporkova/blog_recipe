import unittest
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By


class BasicInstallTest(unittest.TestCase):
    # Однажды Катя была в раздумьях, чтобы такое приготовить
    # Но у нее совершенно не было идей и она решила поискать рецепты в Google
    # Она ввела запрос "Рецепты" и кликнула по одной из ссылок

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.verificationErrors = None

    def setUp(self):  # создается браузер
        self.browser = webdriver.Chrome()
        # self.browser.implicitly_wait(3)

    def tearDown(self):  # закрывается браузер, когда команда выполнена
        self.browser.quit()

    def test_home_page_title(self):
        # Катя попала на сайт по адресу: http://127.0.0.1:8000
        # В заголовке сайта было написано "Рецепты"
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Рецепты', self.browser.title)
        # self.fail('Finish the test!')

    # def test_home_page_header(self):  вот нужно будет сделать проверку на наличие изображения Foodei Blog на главной странице
    #     # В шапке сайта написано "Foodei Blog"
    #     self.browser.get('http://127.0.0.1:8000')
    #     header = self.browser.find_element(By.TAG_NAME, 'img')
    #     # self.assertIn('logo', header.text)
    #     # self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()

# А под шапкой расположен блок с самыми разными рецептами

# У каждого рецепта есть заголовок, описание, ссылка на страницу с полным описанием, а у некоторых еще и список ингредиентов

# Катя кликнула по заголовку и у нее открылась страница с полным описанием рецепта

# Прочитав статью, Катя кликнула по картинке "Foodie Blog" в шапке сайта и попал на Главную страницу.

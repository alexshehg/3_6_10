import time
from selenium.webdriver.common.by import By


def test_visible_button_add_to_cart(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(10)
    button = browser.find_element("css selector", ".btn-add-to-basket")
    assert button is not None, "Кнопки 'Добавить в корзину' нет!"

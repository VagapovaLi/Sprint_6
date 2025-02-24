import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators  import OrderPageLocators
import time
import allure
DZEN_URL ='https://dzen.ru/?yredirect=true'


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем кнопку заказать вверху страницы')
    def check_click_button_top_page(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_ORDER_TOP_OF_THE_PAGE).click()

    @allure.step('Нажимаем кнопку заказать внизу страницы')
    def check_click_button_bottom_page(self):

        element = self.driver.find_element(*OrderPageLocators.BUTTON_ORDER_BUTTON_OF_THE_PAGE)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(OrderPageLocators.BUTTON_ORDER_BUTTON_OF_THE_PAGE)).click()

    @allure.step('Нажимем кнопку "Самокат ')
    def check_click_button_scooter(self):

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.BUTTON_LINK_SCOOTER)).click()
        time.sleep(5)

    @allure.step('Нажимаем на логотип "Яндекс". Переходим в новое окно браузера')
    def click_on_the_yandex_logo_and_switch_window(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.BUTTON_LINK_YANDEX)).click()

        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])
        return WebDriverWait(self.driver, timeout=20).until(EC.url_to_be(DZEN_URL))


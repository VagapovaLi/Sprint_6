import pytest
from selenium import webdriver
from locators.order_page_locators import OrderPageLocators
import allure
from pages.order_page import OrderPage
from pages.base_page import BasePage

MAIN_URL = "https://qa-scooter.praktikum-services.ru/"
DZEN_URL ='https://dzen.ru/?yredirect=true'

class TestOrderPage:
    @pytest.fixture(scope='function')
    def driver(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        yield self.driver
        self.driver.quit()


    @pytest.mark.parametrize("name, surname, address, phone_number, comment", [
        ('Петя', 'Пупкин', 'Пупкинская 8', '89682548955', 'Привозите быстрей'),
    ])

    @allure.title("Заказ сомаката через кнопкк 'Заказть' в вверху страницы с переходом на главную страницу" )
    def test_order_scooter_button_top_page(self, driver, name, surname, address, phone_number, comment):
        order_page = OrderPage(driver)
        base_page = BasePage(driver)
        base_page.check_click_button_top_page()

        order_page.order(name=name, surname=surname, address=address, phone_number=phone_number, comment=comment)

        success_message = driver.find_element(*OrderPageLocators.TEXT_ORDER_SUBMITTED).text
        assert "Заказ оформлен" in success_message

        order_page.check_click_view_status()
        base_page.check_click_button_scooter()
        assert driver.current_url == MAIN_URL


    @pytest.mark.parametrize("name, surname, address, phone_number, comment", [
        ('Вася', 'Иванов', 'Ивановская 10', '89161234567', 'Привозите аккуратней'),
    ])

    @allure.title("Заказ сомаката через кнопкк 'Заказть' в вверху страницы")
    def test_order_scooter_button_bottom_page(self, driver, name, surname, address, phone_number, comment):
        order_page = OrderPage(driver)
        base_page = BasePage(driver)
        base_page.check_click_button_bottom_page()

        order_page.order(name=name, surname=surname, address=address, phone_number=phone_number, comment=comment)

        success_message = driver.find_element(*OrderPageLocators.TEXT_ORDER_SUBMITTED).text
        assert "Заказ оформлен" in success_message

        order_page.check_click_view_status()
        base_page.click_on_the_yandex_logo_and_switch_window()
        assert self.driver.current_url == DZEN_URL, f"Ожидался URL: {DZEN_URL}, но получен: {self.driver.current_url}"
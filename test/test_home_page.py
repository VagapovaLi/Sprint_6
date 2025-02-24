import pytest
from selenium import webdriver
from locators.home_page_locators import HomePageLocators
import allure
from pages.home_page import Dropdownlist
BASE_URL = "https://qa-scooter.praktikum-services.ru/"


class TestDropdownlist:
    @pytest.fixture(scope='function')
    def driver(self):
        self.driver = webdriver.Firefox()
        self.driver.get(BASE_URL)
        yield self.driver
        self.driver.quit()

    @allure.step('Прокрутка к вопросам, окрыть первый вопрос, ответ')
    def test_check_click_1_question(self, driver):

        dropdownlist = Dropdownlist(driver)
        dropdownlist.scroll_to_questions()
        dropdownlist.check_click_1_question()

        element_text = driver.find_element(*HomePageLocators.TEXT_FIRST_RS).text
        assert 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'  in element_text

    @allure.step('Прокрутка к вопросам, окрыть 2 вопрос, ответ')
    def test_check_click_2_question(self, driver):
        dropdownlist = Dropdownlist(driver)
        dropdownlist.scroll_to_questions()
        dropdownlist.check_click_2_question()

        element_text = driver.find_element(*HomePageLocators.TEXT_SECOND_RS).text
        assert 'Пока что у нас так: один заказ — один самокат' in element_text

    @allure.step('Прокрутка к вопросам, окрыть 3 вопрос, ответ')
    def test_check_click_3_question(self, driver):
        dropdownlist = Dropdownlist(driver)
        dropdownlist.scroll_to_questions()
        dropdownlist.check_click_3_question()

        element_text = driver.find_element(*HomePageLocators.TEXT_FHREE_RS).text
        assert 'оформляете заказ на 8 мая' in element_text


    @allure.step('Прокрутка к вопросам, окрыть 4 вопрос, ответ')
    def test_check_click_4_question(self, driver):
        dropdownlist = Dropdownlist(driver)
        dropdownlist.scroll_to_questions()
        dropdownlist.check_click_4_question()

        element_text = driver.find_element(*HomePageLocators.TEXT_4_RS).text
        assert 'Только начиная с завтрашнего дня' in element_text

    @allure.step('Прокрутка к вопросам, окрыть 5 вопрос, ответ')
    def test_check_click_5_question(self, driver):
        dropdownlist = Dropdownlist(driver)
        dropdownlist.scroll_to_questions()
        dropdownlist.check_click_5_question()

        element_text = driver.find_element(*HomePageLocators.TEXT_5_RS).text
        assert 'Пока что нет! Но если что-то срочное' in element_text

    @allure.step('Прокрутка к вопросам, окрыть 6 вопрос, ответ')
    def test_check_click_6_question(self, driver):
        dropdownlist = Dropdownlist(driver)
        dropdownlist.scroll_to_questions()
        dropdownlist.check_click_6_question()

        element_text = driver.find_element(*HomePageLocators.TEXT_6_RS).text
        assert 'Самокат приезжает к вам с полной зарядкой.' in element_text

    @allure.step('Прокрутка к вопросам, окрыть 7 вопрос, ответ')
    def test_check_click_7_question(self, driver):
        dropdownlist = Dropdownlist(driver)
        dropdownlist.scroll_to_questions()
        dropdownlist.check_click_7_question()

        element_text = driver.find_element(*HomePageLocators.TEXT_7_RS).text
        assert 'Да, пока самокат не привезли.' in element_text

    @allure.step('Прокрутка к вопросам, окрыть 8 вопрос, ответ')
    def test_check_click_8_question(self, driver):
        dropdownlist = Dropdownlist(driver)
        dropdownlist.scroll_to_questions()
        dropdownlist.check_click_8_question()

        element_text = driver.find_element(*HomePageLocators.TEXT_8_RS).text
        assert 'Да, обязательно. Всем самокатов! И Москве, и Московской области.' in element_text
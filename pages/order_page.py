import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вводим имя: {name}')
    def check_input_name(self, name):
        self.driver.find_element(*OrderPageLocators.INPUT_NAME).send_keys(name)

    @allure.step('Вводим фамилию: {surname}')
    def check_input_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.INPUT_SURNAME).send_keys(surname)

    @allure.step('Вводим адресс: {address}')
    def check_input_address(self, address):
        self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(address)

    @allure.step('Выбор станцию метро')
    def check_input_station_metro(self):
        self.driver.find_element(*OrderPageLocators.INPUT_METRO_STATION).click()
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(OrderPageLocators.METRO_STATION_CHERKIZOVSKAYA))
        self.driver.find_element(*OrderPageLocators.METRO_STATION_CHERKIZOVSKAYA).click()

    @allure.step('Вводим номер телефлна: {phone_number}')
    def check_input_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.INPUT_PHONE_NUMBER).send_keys(phone_number)

    @allure.step('Нажимаем кнопку далее')
    def check_click_next(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

    @allure.step('Выбираем дату')
    def check_click_date(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(OrderPageLocators.INPUT_SELECT_DATE)).click()
        self.driver.find_element(*OrderPageLocators.SELECT_DATE).click()

    @allure.step('Выбираем срок аренды два дня')
    def check_rental_period_two_days(self):
        self.driver.find_element(*OrderPageLocators.INPUT_RENTAL_PERIOD).click()
        self.driver.find_element(*OrderPageLocators.SELECT_RENTAL_PERIOD_TWO_DAYS).click()


    @allure.step('Выбираем срок аренды четыре дня')
    def check_rental_period_four_days(self):
        self.driver.find_element(*OrderPageLocators.INPUT_RENTAL_PERIOD).click()
        self.driver.find_element(*OrderPageLocators.SELECT_RENTAL_PERIOD_FOUR_DAYS).click()

    @allure.step('Выбираем цвет самоката черный')
    def check_scooter_color_black(self):
        self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_BLACK).click()

    @allure.step('Выбираем цвет самоката черный')
    def check_scooter_color_grey(self):
        self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_GREY).click()

    @allure.step('Вводим комментарий для курьера: {comment}')
    def check_input_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT_FOR_COURIER).click()
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT_FOR_COURIER).send_keys(comment)

    @allure.step('Нажимем кнопку заказть в финале')
    def check_click_next_final(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(OrderPageLocators.BUTTON_ORDER_FINAL)).click()


    @allure.step('Нажимем кнопку "Да" в финале')
    def check_click_yes_final(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(OrderPageLocators.BUTTON_YES_PLACE_ORDER)).click()


    @allure.step('Нажимем кнопку "Посмотреть статус" ')
    def check_click_view_status(self):

        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.BUTTON_VIEW_STATUS)).click()


    def order(self, name, surname, address, phone_number,comment):
        self.check_input_name(name)
        self.check_input_surname(surname)
        self.check_input_address(address)
        self.check_input_station_metro()
        self.check_input_phone_number(phone_number)
        self.check_click_next()
        self.check_click_date()
        self.check_rental_period_two_days()
        self.check_scooter_color_black()
        self.check_input_comment(comment)
        self.check_click_next_final()
        self.check_click_yes_final()


import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import HomePageLocators
import allure


class Dropdownlist:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Прокрутка до "Вопросы о важном"')
    def scroll_to_questions(self):
        element = self.driver.find_element(*HomePageLocators.TEXT_QUESTION_ABOUT_IMPORTANT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(HomePageLocators.TEXT_QUESTION_ABOUT_IMPORTANT))

    @allure.step('Кликаем на первый вопрос, получаем ответ')
    def check_click_1_question(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.CLICK_FIRST_QUESTION)).click()

    def check_click_2_question(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.CLICK_SECOND_QUESTION)).click()

    def check_click_3_question(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.CLICK_FHREE_QUESTION)).click()

    def check_click_4_question(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.CLICK_4_QUESTION)).click()

    def check_click_5_question(self):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.CLICK_5_QUESTION)).click()

    def check_click_6_question(self):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.CLICK_6_QUESTION)).click()

    def check_click_7_question(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.CLICK_7_QUESTION)).click()

    def check_click_8_question(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(HomePageLocators.CLICK_8_QUESTION)).click()



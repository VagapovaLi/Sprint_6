from selenium.webdriver.common.by import By


class BasePageLocators:

    BUTTON_ORDER_TOP_OF_THE_PAGE = (By.XPATH, '//div[1]//div[2]/button[1][text()="Заказать"]')                                     # кнопка заказать в вверху страницы

    BUTTON_LINK_SCOOTER = (By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR')                                                  # кнопка ссылка Самокат
    BUTTON_LINK_YANDEX = (By.CSS_SELECTOR, '.Header_LogoYandex__3TSOI')                                                 # кнопка ссылка Яндекс

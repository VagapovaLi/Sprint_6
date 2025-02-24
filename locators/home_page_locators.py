from selenium.webdriver.common.by import By

class HomePageLocators:

    TEXT_QUESTION_ABOUT_IMPORTANT = (By.XPATH,'//div[text()="Вопросы о важном"]')
    CLICK_FIRST_QUESTION = (By.XPATH,'//div[text()="Сколько это стоит? И как оплатить?"]')                                       #клик по первому вопросу "Сколько это стоит? И как оплатить?"
    TEXT_FIRST_RS = (By.XPATH, '//p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]')                               #ответ на первый влпрос
    CLICK_SECOND_QUESTION = (By.XPATH, '//div[text()="Хочу сразу несколько самокатов! Так можно?"]')
    TEXT_SECOND_RS = (By.XPATH, '//p[contains(text(), "Пока что у нас так: один заказ — один самокат")]')
    CLICK_FHREE_QUESTION = (By.XPATH, '//div[text()="Как рассчитывается время аренды?"]')
    TEXT_FHREE_RS = (By.XPATH, '//p[contains(text(), "оформляете заказ на 8 мая")]')
    CLICK_4_QUESTION = (By.XPATH, '//div[text()="Можно ли заказать самокат прямо на сегодня?"]')
    TEXT_4_RS = (By.XPATH, '//p[contains(text(), "Только начиная с завтрашнего дня. Но скоро станем расторопнее.")]')
    CLICK_5_QUESTION = (By.XPATH, '//div[text()="Можно ли продлить заказ или вернуть самокат раньше?"]')
    TEXT_5_RS = (By.XPATH, '//p[contains(text(), "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.")]')
    CLICK_6_QUESTION = (By.XPATH, '//div[text()="Вы привозите зарядку вместе с самокатом?"]')
    TEXT_6_RS = (By.XPATH, '//p[contains(text(), "Самокат приезжает к вам с полной зарядкой.")]')
    CLICK_7_QUESTION = (By.XPATH, '//div[text()="Можно ли отменить заказ?"]')
    TEXT_7_RS = (By.XPATH, '//p[contains(text(), "Да, пока самокат не привезли.")]')
    CLICK_8_QUESTION = (By.XPATH, '//div[text()="Я жизу за МКАДом, привезёте?"]')
    TEXT_8_RS = (By.XPATH, '//p[contains(text(), "Да, обязательно. Всем самокатов! И Москве, и Московской области.")]')

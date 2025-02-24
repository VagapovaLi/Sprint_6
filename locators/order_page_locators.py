from selenium.webdriver.common.by import By

class OrderPageLocators:

    INPUT_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')                                                            #поле ввода Имя
    INPUT_SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')                                                     #поле ввода Фамилии
    INPUT_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')                                  #поле ввода Адрес
    INPUT_METRO_STATION = (By.XPATH, '//input[@placeholder="* Станция метро"]')                                         #Кнопка для выбора станции метро
    METRO_STATION_CHERKIZOVSKAYA = (By.XPATH, '//div[contains(text(), "Черкизовская")]')                                #Кнопка для выбора станции метро Черкизовская
    INPUT_PHONE_NUMBER = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')                       #поле ввода телефлна
    BUTTON_NEXT= (By.XPATH, '//button[text()="Далее"]')                                                                 #кнопка далее
    INPUT_SELECT_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')                                  #форма для выбора даты,когда привезут сомокат
    SELECT_DATE = (By.XPATH, '//div[@aria-label = "Choose пятница, 28-е февраля 2025 г."]')                             #     ВЫБРАТЬ ДАТУ
    INPUT_RENTAL_PERIOD = (By.XPATH, '//div[text()="* Срок аренды"]')                                                   #форма для выбора срока аренды
    SELECT_RENTAL_PERIOD_TWO_DAYS = (By.XPATH, '//div[text()="двое суток"]')                                            #выбрать срока аренды двое суток
    SELECT_RENTAL_PERIOD_FOUR_DAYS = (By.XPATH, '//div[text()="четверо суток"]')                                        #выбрать срока аренды четверо  суток

    SCOOTER_COLOR_BLACK = (By.XPATH, '//*[@id="black"]' )                                                               #выбрать цвет черный
    SCOOTER_COLOR_GREY = (By.XPATH, '//*[@id="grey"]')                                                                  #выбрать цвет серый
    INPUT_COMMENT_FOR_COURIER = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')                           #форма для коментария для курьера
    BUTTON_ORDER_FINAL = (By.XPATH, '//div//button[2][text()="Заказать"]')                                              #финальная кнопка "Заказать "
    BUTTON_YES_PLACE_ORDER = (By.XPATH, '//button[text()="Да"]')                                                        #кнопка "Да"
    TEXT_ORDER_SUBMITTED = (By.XPATH, '//div[text()="Заказ оформлен"]')                                                 #форма "Заказ оформлен"

    BUTTON_VIEW_STATUS = (By.XPATH, '//button[text()="Посмотреть статус"]')                                              #кнопка "Посмотреть статус"



    BUTTON_ORDER_TOP_OF_THE_PAGE = (By.XPATH, '//div[1]//div[2]/button[1][text()="Заказать"]')                            # кнопка заказать в вверху страницы
    BUTTON_ORDER_BUTTON_OF_THE_PAGE = ( By.XPATH, '//div[4]//button[1][text()="Заказать"]')                                # кнопка внизу  страницы

    BUTTON_LINK_SCOOTER = (By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR')                                                    #кнопка ссылка Самокат
    BUTTON_LINK_YANDEX = (By.CSS_SELECTOR, '.Header_LogoYandex__3TSOI')                                                               #кнопка ссылка Яндекс


from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from lesson_26.widgets.components import Button


class PageButton:
    _instance = None
    URL = "https://rozetka.com.ua/ua/"

    # Singleton pattern
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.button_click_example_xpath_1_loc = (By.XPATH, '//button[@class="header__button ng-star-inserted"]')
        self.button_click_example_xpath_2_loc = (By.XPATH, '//button[@type="button" and @class="header__button '
                                                           'ng-star-inserted"]')
        self.button_click_example_xpath_3_loc = (By.XPATH, '//button[contains(@class, "header__button '
                                                           'ng-star-inserted")]')
        self.button_click_example_xpath_4_loc = (
        By.XPATH, '//li[@class="header-actions__item header-actions__item--user"]//button["button"]')
        self.button_click_example_xpath_5_loc = (
        By.XPATH, '//button[@class="header__button ng-star-inserted" and position()=1]')

        self.button_click_example_css_1_loc = (By.CSS_SELECTOR, "button.header__button.ng-star-inserted")
        self.button_click_example_css_2_loc = (By.CSS_SELECTOR, "button.header__button.ng-star-inserted[type='button']")
        self.button_click_example_css_3_loc = (By.CSS_SELECTOR, "header button.header__button.ng-star-inserted")
        self.button_click_example_css_4_loc = (By.CSS_SELECTOR, "button.header__button.ng-star-inserted:nth-child(1)")
        self.button_click_example_css_5_loc = (By.CSS_SELECTOR,
                                               ".header button.header__button.ng-star-inserted:nth-child(2)")


    def open(self):
        self.driver.get(self.URL)
        return self

    def button_click_example_xpath_1(self):
        return Button(self.driver, self.button_click_example_xpath_1_loc)

    def button_click_example_xpath_2(self):
        return Button(self.driver, self.button_click_example_xpath_2_loc)

    def button_click_example_xpath_3(self):
        return Button(self.driver, self.button_click_example_xpath_3_loc)

    def button_click_example_xpath_4(self):
        return Button(self.driver, self.button_click_example_xpath_4_loc)

    def button_click_example_xpath_5(self):
        return Button(self.driver, self.button_click_example_xpath_5_loc)

    def button_click_example_css_1(self):
        return Button(self.driver, self.button_click_example_css_1_loc)

    def button_click_example_css_2(self):
        return Button(self.driver, self.button_click_example_css_2_loc)

    def button_click_example_css_3(self):
        return Button(self.driver, self.button_click_example_css_3_loc)

    def button_click_example_css_4(self):
        return Button(self.driver, self.button_click_example_css_4_loc)

    def button_click_example_css_5(self):
        return Button(self.driver, self.button_click_example_css_5_loc)







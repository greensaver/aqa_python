from selenium.webdriver.remote.webelement import WebElement
from lesson_20.conftest import chrome
from lesson_20.DynamicPropertiesPage import PageDynamicProperties
from lesson_20.ElementsPage import ElementsPage
import pytest


class TestElementsPage:
    def test_page(self, firefox):
        page = ElementsPage(firefox)
        page.open()
        elements = page.get_elements_page_categories()
        assert len(elements) == 33

    @pytest.mark.parametrize("expected_category", ['Text Box', 'Check Box', 'Radio Button', 'Web Tables', 'Buttons',
                                                   'Links', 'Broken Links - Images', 'Upload and Download',
                                                   'Dynamic Properties', '', '', '', '', '', '', '', '', '', '', '',
                                                   '', '', '', '', '', '', '', '', '', '', '', '', ''])
    def test_elements_value(self, chrome, expected_category):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert expected_category in elements

    # def test_is_button_enabled(self, chrome):
    #     page = PageDynamicProperties(chrome)
    #     page.open()
    #     button: WebElement = page.disable_enable_button()
    #     button.click()
    #
    # def test_is_button_shown(self, chrome):
    #     page = PageDynamicProperties(chrome).open()  # короткий запис
    #     button: WebElement = page.button_invisible_visible()
    #     button.click()
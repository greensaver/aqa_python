from lesson_18.TextBoxPage import TextBoxPage
from lesson_18.conftest import chrome

class TestTextBox:

    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Serhii")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_fullname()
        assert name_field.replace("Name:", "") == "Serhii"

    def test_email_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_email_field("greensaver.ua@gmail.com")
        page.scroll_down()
        page.click_submit()
        email_field = page.get_result_email()
        assert email_field.replace("Email:", "") == "greensaver.ua@gmail.com"

    def test_curr_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_current_address_field("Tatarska street")
        page.scroll_down()
        page.click_submit()
        current_address_field = page.get_result_current_address()
        assert current_address_field.replace("Current Address :", "") == "Tatarska street"

    def test_perm_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_permanent_address_field("Doncha street")
        page.scroll_down()
        page.click_submit()
        permanent_address_field = page.get_result_permanent_address()
        assert permanent_address_field.replace("Permananet Address :", "") == "Doncha street"

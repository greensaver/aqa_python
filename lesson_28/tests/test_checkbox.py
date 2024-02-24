import pytest
from lesson_28.src.pages.page_checkbox import CheckboxPage
from lesson_28.conftest import chrome_class


@pytest.mark.usefixtures("chrome_class")
class TestCheckboxPage:
    def setup(self):
        self.page = CheckboxPage(self.driver)

    def test_page(self):
        self.page.open()
        self.page.expand_folder("home")
        self.page.expand_folder("desktop")
        self.page.mark_folder("commands")
        self.page.expand_folder("documents")
        self.page.mark_folder("office")
        pass

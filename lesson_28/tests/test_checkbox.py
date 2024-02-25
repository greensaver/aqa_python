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
        assert self.page.is_folder_expanded("home"), "Failed to expand 'home' folder"
        self.page.expand_folder("desktop")
        assert self.page.is_folder_expanded("desktop"), "Failed to expand 'desktop' folder"
        self.page.mark_folder("commands")
        assert self.page.is_folder_marked("commands"), "Failed to mark 'commands' folder"
        self.page.expand_folder("documents")
        assert self.page.is_folder_expanded("documents"), "Failed to expand 'documents' folder"
        self.page.mark_folder("office")
        assert self.page.is_folder_marked("office"), "Failed to mark 'office' folder"

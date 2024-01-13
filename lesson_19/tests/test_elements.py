import pytest
from lesson_19.conftest import chrome
from lesson_19.ElementsPage import ElementsPage


class TestElementsPage:
    def test_page(self, chrome):
        page = ElementsPage(chrome)
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

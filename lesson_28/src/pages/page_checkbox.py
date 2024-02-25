from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

URL = "https://demoqa.com/checkbox"

class CheckboxPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(URL)
        return self

    def expand_folder(self, name) -> None:
        versatile_checkbox_button = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]//ancestor::span/button")
        versatile_checkbox_button.click()

    def is_folder_expanded(self, name):
        try:
            xpath_expression = f"//*//label[@for='tree-node-{name}']//parent::span/button[contains(@class, 'rct-collapse-btn') and contains(@class, 'rct-collapse')]"
            versatile_checkbox_button = self.driver.find_element(By.XPATH, xpath_expression)
            print(f"Found button for '{name}' using XPath: {xpath_expression}")
            return True
        except NoSuchElementException:
            print(f"Button for '{name}' not found using XPath: {xpath_expression}")
            return False

    def collapse_folder(self, name) -> None:
        versatile_checkbox_button = self.driver.find_element(By.XPATH,
                                                             f"//label[contains(@for, 'tree-node-{name}')]//ancestor::span/button")
        versatile_checkbox_button.click()

    def mark_folder(self, name):
        versatile_checkbox_button = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]")
        input_field = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]/input")
        if not input_field.is_selected():
            versatile_checkbox_button.click()

    def is_folder_marked(self, name):
        xpath_expression = f"//label[@for='tree-node-{name}']/input[@type='checkbox']"
        try:
            checkbox = self.driver.find_element(By.XPATH, xpath_expression)
            print(f"Found checkbox for '{name}' using XPath: {xpath_expression}")
            return checkbox.is_selected()
        except NoSuchElementException:
            print(f"Checkbox for '{name}' not found using XPath: {xpath_expression}")
            return False

    def unmark_folder(self, name):
        versatile_checkbox_button = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]")
        versatile_checkbox_button.click()

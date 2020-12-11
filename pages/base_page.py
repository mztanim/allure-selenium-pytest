from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class BasePage:
    url = "https://opensource-demo.orangehrmlive.com/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def load(self):
        self.driver.get(self.url)

    def _get_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def _input_text(self, locator, text):
        self._get_element(locator).send_keys(text)

    def _click_element(self, locator):
        self._get_element(locator).click()


    def _get_text(self, locator):
        return self._get_element(locator).text

    def get_url(self):
        return self.driver.current_url

    def _get_element_from_elements_by_text(self, locator, text):
        elements = self.wait.until(ec.visibility_of_any_elements_located(locator))
        for element in elements:
            if element.text == text:
                return element

    def _select_by_text(self, locator, text):
        select = Select(self._get_element(locator))
        select.select_by_visible_text(text)


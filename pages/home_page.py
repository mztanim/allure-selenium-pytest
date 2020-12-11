from selenium.webdriver.common.by import By

from pages.menu_page import MenuBar


class HomePage(MenuBar):
    url = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"

    # HomePage locators
    plt_welcome_msg = By.PARTIAL_LINK_TEXT, "Welcome "

    def get_wel_msg(self):
        return self._get_element(self.plt_welcome_msg).text



from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MenuBar(BasePage):
    # locator:
    __welcome_text = By.ID, "welcome"
    __about_link = By.ID, "aboutDisplayLink"
    __logout_link = By.LINK_TEXT, "Logout"

    __menu_loc = {
        "Admin": {
            "Admin": (By.ID, "menu_admin_viewAdminModule"),
            "User Management": (By.ID, "menu_admin_UserManagement"),
            "Users": (By.ID, "menu_admin_viewSystemUsers"),
            "Nationalities": (By.ID, "menu_admin_nationality")
        },
        "PIM": {
            "PIM": (By.ID, "menu_pim_viewPimModule"),
            "Add Employee": (By.ID, "menu_pim_addEmployee")
        }

    }

    __first_level_menu = By.CSS_SELECTOR, ".firstLevelMenu"
    __second_level_menu = By.CSS_SELECTOR, ".firstLevelMenu+ul>li"
    __third_level_menu = By.CSS_SELECTOR, ".firstLevelMenu+ul>li>ul>li"

    __menu_locators = [__first_level_menu, __second_level_menu, __third_level_menu]

    def get_welcome_msg(self):
        return self._get_text(self.__welcome_text)

    def logout(self):
        self._click_element(self.__welcome_text)
        self._click_element(self.__logout_link)
        return BasePage(self.driver).get_url()

    def navigate_to_menu_by_loc(self, menus):  # Admin_User Management_Users
        menus = menus.split("_")  # ["Admin", "User Management", "Users]

        loc = self.__menu_loc[menus[0]]  # menus[0] = "Admin", menu_loc["Admin"]

        actions = ActionChains(self.driver)
        for i in range(len(menus) - 1):  # ["Admin", "User Management"]
            actions.move_to_element(self._get_element(loc[menus[i]])).perform()

        # find and click the last item   #Users
        self._click_element(loc[menus[-1]])

        return BasePage(self.driver).get_url()


    def navigate_to_menu_by_dynamic_loc(self, menus):
        menus = menus.split(",")

        actions = ActionChains(self.driver)
        for i in range(len(menus) - 1):
            element = self._get_element_from_elements_by_text(self.__menu_locators[i], menus[i])
            actions.move_to_element(element).perform()

        element = self._get_element_from_elements_by_text(self.__menu_locators[len(menus) - 1], menus[-1])
        element.click()

        return BasePage(self.driver).get_url()

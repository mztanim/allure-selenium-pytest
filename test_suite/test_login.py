import pytest
import allure
import time

from allure_commons.types import AttachmentType
from pages.login_page import LoginPage
from data_generator import login_page_test_data as login_data


@pytest.mark.usefixtures("driver_init")
class TestLogin:
    data = login_data.get_login_testdata()
    driver = None

    @pytest.fixture(autouse=True)
    def load_url(self, driver_init):
        self.logger.info("Test_case_started")
        self.driver.delete_all_cookies()
        self.login_page = LoginPage(self.driver)
        self.logger.info("Loading Login Page")
        self.login_page.load()
        yield
        self.logger.info("Test_case_completed")


    @pytest.mark.parametrize('username,password,expected_msg', data['login_pass_data'])
    def test_login_pass(self, username, password, expected_msg):
        #self.logger.debug(f"username = {username}, password = {password}")
        home_page = self.login_page.login_pass(username, password)
        #self.logger.debug(f"welcome_msg = {home_page.get_wel_msg()}")
        assert expected_msg in home_page.get_wel_msg()

    @pytest.mark.parametrize('username,password,expected_msg', data['login_fail_data'])
    def test_login_fail(self, username, password, expected_msg):
        self.login_page.login_fail(username, password)
        try:
            actual_msg = self.login_page.get_err_msg()
            assert actual_msg == expected_msg
        except AssertionError as e:
            self.logger.exception(e.__traceback__)
            time_str = time.strftime("%Y%m%d-%H%M%S")
            allure.attach(self.driver.get_screenshot_as_png(), name=f"login_fail_{time_str}",
                          attachment_type=AttachmentType.PNG)
            pytest.fail()



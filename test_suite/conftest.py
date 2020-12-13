import pytest
import os
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# pytest_addoption - adding a cmd line variable
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")



@pytest.fixture(scope="session")
def driver_init(request, pytestconfig):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    if not (os.path.exists("../target/logs")):
        os.makedirs("../target/logs")
    file_name = os.path.join(os.path.dirname(__file__), '..', 'target', 'logs', 'test_log.log')
    formatter = logging.Formatter('%(asctime)12s: %(name)s: %(levelname)s: %(message)s')

    file_handler = logging.FileHandler(file_name, mode='w')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)


    browser = pytestconfig.getoption('browser')

    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())

    logger.info(f"Starting the '{browser.upper()}' browser")

    #request.cls.driver = driver

    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"driver",driver)
        setattr(cls.obj, "logger", logger)
    yield 

    driver.close()
    if driver is not None:
        driver.quit()






# session, module, class, function

#conftest.py
#pytest_addoption()
#@pytest.fixture(scope)


# readingColumnNumber excelsheet by columnheader
# reading data from config file
# how to log

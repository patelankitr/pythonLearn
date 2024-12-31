import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup():
    """Set up WebDriver instance for each test."""
    driver = webdriver.Chrome()
    driver.get('https://www.supremacy1914.com')
    driver.maximize_window()
    yield driver
    driver.quit()
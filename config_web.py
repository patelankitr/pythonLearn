import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def setup():
    """Set up WebDriver instance for each test with headless Chrome."""
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    chrome_options.add_argument('--no-sandbox')  # For running in certain environments (like CI/CD)
    chrome_options.add_argument('--disable-dev-shm-usage')  # For certain Linux environments

    # Initialize the WebDriver with options
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get('https://www.supremacy1914.com')
    driver.maximize_window()

    yield driver

    driver.quit()
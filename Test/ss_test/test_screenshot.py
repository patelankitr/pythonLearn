import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.screenshot_page import take_element_screenshot, compare_element_images
from config_web import setup


def test_supremacy_automation(setup, request):
    driver = setup
    take_screenshot = request.config.getoption("--take-screenshot")  # Get the string ("True" or "False")

    # Convert the string to a boolean
    take_screenshot = take_screenshot.lower() == "true"  # Convert to True if "True" is passed

    # Step 1: Handle the "Agree and Close" popup
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'didomi-notice-agree-button'))
        )
        agree_button = driver.find_element(By.ID, 'didomi-notice-agree-button')

        # Case 1: If take_screenshot is True, take a screenshot and compare
        if take_screenshot:
            agree_button_path = take_element_screenshot(driver, agree_button, "agree_button")
            assert compare_element_images("agree_button.png"), "Agree button does not match the baseline!"
        # Case 2: If take_screenshot is False, just compare the screenshot without taking a new one
        else:
            assert compare_element_images("agree_button.png"), "Agree button does not match the baseline!"

        agree_button.click()
    except Exception as e:
        print(f"Agree and close button not found: {e}")

    # Step 2: Login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'loginbox_login_input')))
    driver.find_element(By.ID, "loginbox_login_input").send_keys("raven_flame")
    driver.find_element(By.ID, "loginbox_password_input").send_keys("Ankit007")
    driver.find_element(By.ID, "func_loginbutton").click()
    time.sleep(10)

    # Step 3: Handle the login iframe popup
    driver.switch_to.frame("ifm")
    try:
        popup = driver.find_element(By.XPATH, "//div[@class='button_close func_close_button']")

        # Case 1: If take_screenshot is True, take a screenshot and compare
        if take_screenshot:
            popup_screenshot_path = take_element_screenshot(driver, popup, "popup_close_button")
            print(f"Popup screenshot saved at: {popup_screenshot_path}")
            assert compare_element_images("popup_close_button.png"), "Popup close button does not match the baseline!"
        # Case 2: If take_screenshot is False, just compare the screenshot without taking a new one
        else:
            assert compare_element_images("popup_close_button.png"), "Popup close button does not match the baseline!"

        popup.click()
        print("Popup handled successfully.")
    except Exception as e:
        print(f"Error handling popup: {e}")

    time.sleep(10)
    driver.find_element(By.XPATH, "(//div[@class='button_close func_close_button'])[1]").click()
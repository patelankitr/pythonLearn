# config.py
import os
from pathlib import Path
from appium import webdriver
from alttester import AltDriver
from appium.options.common import AppiumOptions




def root_path():
    # Assuming this function returns the project root path
    root = get_project_root()
    apk_directory = f"{root}astrocade_automation\\app\\"

    # Find and return the APK file path
    for file_name in os.listdir(apk_directory):
        if file_name.endswith('.apk'):
            apk_file_path = f"{apk_directory}{file_name}"
            print(f"APK file name: {apk_file_path}")
            return apk_file_path
    return None  # Return None if no APK file is found


def get_project_root() -> Path:
    return Path(__file__).parent.parent


# Device configuration (parameters for Appium initialization)
device_config = {
    'device_name': 'emulator-5554',
    'platform_version': '11',
    'app_path': root_path(),
    'no_reset': True
}


# Parameterized function to initialize Appium driver
def init_appium_driver(device_name, platform_version, app_path, no_reset=True):
    desired_caps = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'deviceName': device_name,
        'platformVersion': platform_version,
        'app': app_path,
        'noReset': no_reset,
    }
    appium_driver = webdriver.Remote("http://127.0.0.1:4723", options=AppiumOptions().load_capabilities(desired_caps))
    return appium_driver


# Function to initialize AltTester driver
def init_alt_tester_driver(host="127.0.0.1", port=13000, app_name="__default__"):
    alt_tester_driver = AltDriver(host=host, port=port, app_name=app_name)
    return alt_tester_driver



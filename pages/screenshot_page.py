import os
from PIL import Image, ImageChops
import allure


def ensure_screenshot_folder_exists(folder):
    """Ensure the folder for screenshots exists."""
    screenshot_dir = os.path.join("D:/Projects/pythonLearn/Test/screenshots", folder)
    os.makedirs(screenshot_dir, exist_ok=True)
    return screenshot_dir


def take_element_screenshot(driver, element, screenshot_name, folder="dynamic"):
    """Capture a screenshot of a specific element and save it to the specified folder."""
    screenshot_dir = ensure_screenshot_folder_exists(folder)
    screenshot_path = os.path.join(screenshot_dir, f"{screenshot_name}.png")

    # Capture screenshot of the element
    element.screenshot(screenshot_path)

    # Attach screenshot to Allure report
    with open(screenshot_path, 'rb') as file:
        allure.attach(file.read(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)

    return screenshot_path


def compare_element_images(dynamic_image_name, baseline_folder="baseline", dynamic_folder="dynamic"):
    """Compare a dynamically captured image of a specific element with the baseline image."""
    baseline_image_path = os.path.join("D:/Projects/pythonLearn/Test/screenshots", baseline_folder, dynamic_image_name)
    print(f"baseline_image_path: {baseline_image_path}")
    dynamic_image_path = os.path.join("D:/Projects/pythonLearn/Test/screenshots", dynamic_folder, dynamic_image_name)
    print(f"dynamic_image_path: {dynamic_image_path}")
    if not os.path.exists(baseline_image_path):
        raise FileNotFoundError(f"Baseline image not found: {baseline_image_path}")

    if not os.path.exists(dynamic_image_path):
        raise FileNotFoundError(f"Dynamic image not found: {dynamic_image_path}")

    # Attach baseline and dynamic images to Allure report
    with open(baseline_image_path, 'rb') as file:
        allure.attach(file.read(), name=f"Baseline - {dynamic_image_name}--Expected Result", attachment_type=allure.attachment_type.PNG)
    with open(dynamic_image_path, 'rb') as file:
        allure.attach(file.read(), name=f"Dynamic - {dynamic_image_name}--Actual Result", attachment_type=allure.attachment_type.PNG)

    # Open the images
    baseline_image = Image.open(baseline_image_path)
    dynamic_image = Image.open(dynamic_image_path)

    # Compare the images
    diff = ImageChops.difference(baseline_image, dynamic_image)
    if diff.getbbox() is None:
        print(f"PASS: The images match for {dynamic_image_name}")
        return True
    else:
        # Save the diff image for debugging
        diff_path = os.path.join("D:/Projects/pythonLearn/Test/screenshots", dynamic_folder, f"{dynamic_image_name}_diff.png")
        diff.save(diff_path)
        print(f"FAIL: The images do not match for {dynamic_image_name}. Diff saved at {diff_path}")
        return False

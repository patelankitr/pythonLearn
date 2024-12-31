
echo "Execute tests..."
pytest -v /var/lib/jenkins/workspace/pythonLearn/Test/ss_test/test_screenshot.py --alluredir=allure-report --take-screenshot=False

echo "Generate Allure report..."
allure serve allure-report

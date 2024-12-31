
echo "Execute tests..."
pytest -v /var/lib/jenkins/workspace/pythonLearn/Test/ss_test/test_screenshot.py --alluredir=allure-report --take-screenshot=False

echo "Generate Allure report..."
allure generate -c allure-report -o allure-results-html

echo "Combine Allure report..."
allure-combine ./allure-results-html

echo "Report generated at: http://localhost:63342/pythonLearn/allure-results-html/index.html"

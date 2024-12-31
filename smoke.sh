
echo "Clearing allure-report folder..."
rm -rf allure-report

echo "Execute tests..."
pytest -v /var/lib/jenkins/workspace/pythonLearn/Test/ss_test/test_screenshot.py --alluredir=allure-report --take-screenshot=False

echo "Generate Allure report..."
allure generate -c allure-report -o allure-results-html

echo "Combine Allure report..."


echo "Report generated at: /var/lib/jenkins/workspace/pythonLearn/allure-results-html/index.html"

# conftest.py
def pytest_addoption(parser):
    parser.addoption(
        "--take-screenshot", action="store", default="False", help="Set True or False to enable screenshot"
    )

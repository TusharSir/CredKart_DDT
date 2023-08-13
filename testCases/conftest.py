import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options


# In pytest, hook functions are functions that can be used to extend or
# modify the behavior of pytest. They are called automatically by pytest at
# specific times during the test run.

# The pytest_configure function is a hook function in pytest that is called once the
# configuration object has been created and all plugins and initial conftest files have been loaded.

# The pytest_addoption function is a hook function in pytest that is used to add custom command-line options to the
# pytest command. It takes a single argument, parser, which is an instance of the argparse.ArgumentParser class.



# add arg --broswer this for your command linner
def pytest_addoption(parser):
    parser.addoption("--browser")


# passing the value to --browser
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Define the browser fixture function with a single argument, request.
# Within the browser function, use the request.config.getoption() method to get the value
# of the --browser option passed to pytest on the command line.


# here we are passing actual value to --browser
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        options = Options()
        options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        driver = webdriver.Firefox(options=options)
        print("Launching Firefox Browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser")
    else:
        print("headlessmode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        #driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://automation.credence.in")
    return driver

# The pytest_metadata function is a hook function in pytest that allows you to
# add custom metadata to the test report. This metadata can be used to provide
# additional information about the test run, such as the environment, the test data,
# or any other relevant information.

def pytest_metadata(metadata):
    # To Add
    metadata["Class"] = "Credence"
    metadata["Batch"] = "CT#15"
    metadata["URL"] = "https://automation.credence.in"
    # To Remove
    metadata.pop("Platform", None)


# How to edit Summary in html report this is your today's task

# use parameter when you have small data set
@pytest.fixture(params=[
    ("Credencetest@test.com", "Credence@123"),
    ("Credencetest@test.com1", "Credence@123"),
    ("Credencetest@test.com", "Credence@1231"),
    ("Credencetest@test.com1", "Credence@1231")
])
def getDataforLogin(request):
    return request.param

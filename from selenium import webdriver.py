from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the target browsers and their WebDriver executables
browsers = [
    {"browserName": "Chrome", "executable_path": "/path/to/chromedriver"},
    {"browserName": "Edge", "executable_path": "/path/to/msedgedriver"},
    {"browserName": "Firefox", "executable_path": "/path/to/geckodriver"}
    # Add more browsers here as needed
]

# Define the URL of the website to be tested
website_url = "http://nj-uat.qaserverix.co:3000/"

# Define the tests to be performed
def test_button_clicks(driver):
    try:
        # Perform the necessary actions to test the buttons
        driver.get(website_url)

        # Find all the buttons on the page
        buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))

        # Click each button
        for button in buttons:
            button.click()
            # Add additional assertions or validation steps here

        # Print the test result
        print(f"{driver.name} button click test passed.")

    except Exception as e:
        print(f"{driver.name} button click test failed: {str(e)}")

# Perform browser compatibility testing
for browser in browsers:
    browser_name = browser["browserName"]
    executable_path = browser["executable_path"]

    print(f"Running button click test for {browser_name}...")

    try:
        if browser_name == "Chrome":
            options = ChromeOptions()
            service = Service(executable_path)
            driver = webdriver.Chrome(service=service, options=options)
        elif browser_name == "Edge":
            options = EdgeOptions()
            service = EdgeService(executable_path)
            driver = webdriver.Edge(service=service, options=options)
        elif browser_name == "Firefox":
            options = FirefoxOptions()
            service = FirefoxService(executable_path)
            driver = webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        # Run the button click test
        test_button_clicks(driver)

    except Exception as e:
        print(f"Failed to run button click test for {browser_name}: {str(e)}")

    finally:
        # Quit the WebDriver session
        driver.quit()

    print(f"Button click test for {browser_name} completed.\n")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Specify the web browsers to test
browsers = ['chrome', 'firefox', 'safari']

# Define the website URL to test
website_url = 'http://nj-uat.qaserverix.co:3000/'

# Loop through each browser and perform the compatibility test
for browser in browsers:
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'safari':
        driver = webdriver.Safari()

    # Open the web browser and navigate to the website
    driver.get(website_url)

    # Perform tests on the website
    # Add your specific test scenarios here

    # Example: Check if a specific element is present on the page
    element = driver.find_element_by_id('element_id')
    if element:
        print(f"{browser}: Element found on the page")
    else:
        print(f"{browser}: Element not found on the page")

    # Example: Fill out a form and submit
    driver.find_element_by_id('name_input').send_keys('John Doe')
    driver.find_element_by_id('email_input').send_keys('johndoe@example.com')
    driver.find_element_by_id('submit_button').click()

    # Close the web browser
    driver.quit()

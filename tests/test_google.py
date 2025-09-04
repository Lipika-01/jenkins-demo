from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_title():
    # Start Chrome browser
    driver = webdriver.Chrome()

    # Open Google
    driver.get("https://www.google.com")

    # Check if "Google" is in title
    assert "Google" in driver.title

    # Close browser
    driver.quit()

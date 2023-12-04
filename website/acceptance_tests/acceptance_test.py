from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# URL of your Flask app
BASE_URL = "http://127.0.0.1:5000"

# User credentials for testing
EMAIL = "jkb389@nau.edu"
PASSWORD = "12341234"

# Set up Selenium WebDriver (assuming Chrome for this example)
driver = webdriver.Chrome()

try:
    # Step 1: Open the website and click on the login button
    driver.get(BASE_URL)
    login_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Login")
    login_button.click()

    # Give some time for the page to load
    time.sleep(2)

    # Step 2: Sign in using the given username and password
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "pass"))
    )

    email_input.send_keys(EMAIL)
    password_input.send_keys(PASSWORD)

    # Step 3: Click the submit button
    submit_button = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "submit"))
    )
    submit_button.click()

    # Give some time for the login process to complete (you might want to use WebDriverWait)
    time.sleep(2)

    # Step 4: Click on the recipes button
    recipes_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Recipes"))
    )
    recipes_button.click()

    # Give some time for the page to load
    time.sleep(2)

    # Step 5: Go into the allergies search area and type in "beef"
    allergies_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "allergies"))
    )
    allergies_input.clear()  # Clear any existing text
    allergies_input.send_keys("beef")  # Type "nuts" into the field
    allergies_input.send_keys(Keys.RETURN)  # Press Enter

    # Give some time for the search process to complete (you might want to use WebDriverWait)
    time.sleep(2)

    # Step 6: Click on the cost checkbox
    cost_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cost"))
    )
    cost_checkbox.click()

    # Step 7: Click on the search button
    search_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "button"))  # Adjust to match your actual link text
    )
    search_button.click()

    # Step 8: Click on the recipe called "Potato Salad"
    potato_salad_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Potato Salad"))
    )
    potato_salad_link.click()

    # Give some time for the recipe page to load
    time.sleep(2)

    # Step 9: Click on the favorite checkbox
    favorite_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "favorite"))  # Replace with the actual ID attribute of the favorite checkbox
    )
    favorite_checkbox.click()

    # Step 10: Click on the planned checkbox
    planned_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "plan"))  # Replace with the actual ID attribute of the planned checkbox
    )
    planned_checkbox.click()

    # Give some time for the checkboxes to update
    time.sleep(2)

    # Step 11: Click on the submit button
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "button"))  # Replace with the actual class attribute of the submit button
    )
    submit_button.click()

    # Step 12: Go to the dashboard page by clicking on the dashboard button
    dashboard_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Dashboard"))
    )
    dashboard_button.click()

    # Give some time for the dashboard page to load
    time.sleep(2)

    # Step 13: Sign out
    sign_out_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Sign Out"))
    )
    sign_out_button.click()

    # Give some time for the sign-out process to complete
    time.sleep(2)

finally:
    # Close the browser window at the end
    driver.quit()

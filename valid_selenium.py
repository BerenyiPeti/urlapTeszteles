from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Load the page with the form to test
driver.get("https://agnes-milia.github.io/urlap_validalas/")

# Find the form fields and submit button
name_field = driver.find_element(By.NAME,"nev")
pw_field = driver.find_element(By.NAME,"jelszo")
email_field = driver.find_element(By.NAME,"email")
submit_button = driver.find_element(By.XPATH,"//input[@type='submit']")

# Fill in the form fields with test data
def teszt(filenev, teszteset, bongeszo):
    if bongeszo == "F":
        driver = webdriver.Firefox()

    lines = []
    with open(filenev) as file_in:

        for line in file_in:
            lines.append(line)

    for line in lines:
        print(line)
    #name_field.send_keys(nev)
    #email_field.send_keys(email)
    #pw_field.send_keys(jelszo)


# Click the submit button
submit_button.click()

# Wait for the page to load after submitting the form
driver.implicitly_wait(10)

# Check if the form submission was successful
success_message = driver.find_element(By.XPATH,"//div[@class='success-message']")
if not success_message.is_displayed():
    raise AssertionError(f"...")
# Close the browser window
driver.quit()


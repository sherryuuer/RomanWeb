# get data from python.org then put it into a dictionary.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "sherryxxxx@gmai.com"
ACCOUNT_PASSWORD = 'xxxxxxxx'
PHONE = "xxxxxxxxxx"


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

url = "https://www.linkedin.com/jobs/search/?currentJobId=3725276027&f_AL=true&f_E=2&f_WT=2&geoId=91000004&keywords=remote&location=%E4%BA%9A%E5%A4%AA%E5%8F%8A%E6%97%A5%E6%9C%AC%E5%9C%B0%E5%8C%BA&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true"

driver.get(url=url)

# Reject Cookies Button
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

# Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")

# # simple application from 53 to 66
# # Locate the apply button
# time.sleep(5)
# apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
# apply_button.click()

# # fill in the number.
# time.sleep(5)
# phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
# if phone.text == "":
#     phone.send_keys(PHONE)

# # Submit the application
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
# submit_button.click()

# Get Listings
time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

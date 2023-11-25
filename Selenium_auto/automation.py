from selenium import webdriver
from selenium.webdriver.common.by import By


# create an option object
chrome_options = webdriver.ChromeOptions()
# keep open
chrome_options.add_experimental_option("detach", True)
# create a driver
chrome_browser = webdriver.Chrome(options=chrome_options)
print(chrome_browser)

chrome_browser.maximize_window()

# website for selenium test: https://demo.seleniumeasy.com
url = 'https://demo.seleniumeasy.com/basic-first-form-demo.html'
chrome_browser.get(url=url)

# test string in the title
if 'Selenium Easy' in chrome_browser.title:
    print("OK")
# test string in the page source
if 'Selenium Easy' in chrome_browser.page_source:
    print("OK")

# button
# full xpath
button = chrome_browser.find_element(
    by=By.XPATH, value="/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button")
# OR css selector
button = chrome_browser.find_element(by=By.CSS_SELECTOR, value=".btn-primary")
print(button.get_attribute('innerHTML'))  # got the button text

# Enter blank space
Enter_message = chrome_browser.find_element(by=By.ID, value="user-message")
Enter_message.clear()
Enter_message.send_keys('Great!')
# click the button above
button.click()


# chrome_browser.quit()  # close the app but need to see the result, so comment outed.

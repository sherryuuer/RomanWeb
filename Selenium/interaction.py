# get data from python.org then put it into a dictionary.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# # click.
# articlecount = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # //*[@id="articlecount"]/a[1]
# # print(articlecount.text)
# click_link = driver.find_element(By.LINK_TEXT, "Talk")
# # click it
# # articlecount.click()
# click_link.click()

# # input
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# the chellage, as we can not access Angela's site, I do this without run it.
url = "xxx"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
submit = driver.find_element(By.CSS_SELECTOR, "form button")

fname.send_keys("Sally")
lname.send_keys("Wong")
email.send_keys("sherry@gmail.com")
submit.click()

# next pj:https://orteil.dashnet.org/cookieclicker/
# driver.close()  # close the page
driver.quit()  # close the app

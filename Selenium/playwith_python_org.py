# get data from python.org then put it into a dictionary.
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://www.python.org/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-text-price")
event_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget div ul li time")
event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget div ul li a")
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time/span
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a
dic = {}
for i in range(5):
    dic[i] = {"time": event_time[i].text, "name": event_name[i].text}
print(dic)

# driver.close()  # close the page
driver.quit()  # close the app

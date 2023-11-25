# sandbox
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://www.amazon.com/All-new-Essentials-including-Graphite-Amazon/dp/B07RQNBBL8/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.b9deb6fa-f7f0-4f9b-bfa0-824f28f79589&keywords=Kindle+E-readers&pd_rd_r=05126364-1902-4cdf-a780-290580562f8b&pd_rd_w=ir0Vi&pd_rd_wg=MMIRB&pf_rd_p=b9deb6fa-f7f0-4f9b-bfa0-824f28f79589&pf_rd_r=1V6H1HYQJE5XKETWT5ST&qid=1695702818&sr=8-1"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-text-price")
price_dollar = driver.find_element(By.XPATH, value='//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]')

print(f"The price is {price_dollar.text}.")

# driver.close()  # close the page
driver.quit()  # close the app

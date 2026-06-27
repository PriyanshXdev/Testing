from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.suryasangam.com/")

driver.find_element(By.XPATH,'//*[@id="surya-calculator"]/div[2]/div[2]/div[2]/div[1]/div/div/input').send_keys("delhi")

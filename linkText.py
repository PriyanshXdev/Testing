from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.google.com")

driver.find_element(By.LINK_TEXT,'Gmail').click()

driver.find_element(By.CLASS_NAME,"button__content").click()

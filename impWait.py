from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.itlearn360.com/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="navLogin"]').click()
driver.find_element(By.ID,"loginEmail").send_keys("priyanshukardam223@gmail.com")
driver.find_element(By.ID,"loginPassword").send_keys("12345")
driver.find_element(By.CLASS_NAME,'lms-btn').click()

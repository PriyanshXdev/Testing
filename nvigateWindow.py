
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://www.google.com/")
driver.switch_to.new_window()
driver.get("https://www.suryasangam.com/")
numberTab=len(driver.window_handles)
print(numberTab)

tabValue=driver.window_handles
print(tabValue)

currentTab=driver.current_window_handle
print(currentTab)

driver.find_element(By.XPATH,'/html/body/main/div[1]/div[2]/div[1]/a/button').click()
firstTab=tabValue[0]

if currentTab!=firstTab:
    driver.switch_to.window(firstTab)

driver.find_element(By.XPATH,'//*[@id="gb"]/div[1]/div[1]/a').click()
print("finished")

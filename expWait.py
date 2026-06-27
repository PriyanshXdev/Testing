from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options=Options()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("https://www.itlearn360.com/")



wait=WebDriverWait(driver,20)

wait.until(
    EC.invisibility_of_element_located((By.ID, "appLoader")))

element=wait.until(EC.element_to_be_clickable((By.ID,"navLogin")))
element.click()
wait.until(
    EC.visibility_of_element_located((By.ID, "loginEmail"))
).send_keys("priyanshu223@gmail.com")

driver.find_element(By.ID,"loginPassword").send_keys("12345")
driver.find_element(By.CLASS_NAME,'lms-btn').click()

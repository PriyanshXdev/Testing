from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo/input.html")
rightClick=driver.find_element(By.XPATH,'/html/body/div/section/div/div/div/p/span')
action=ActionChains(driver)
action.context_click(rightClick).perform()
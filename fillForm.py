# you can choose any single type and submit it dircetly but I choose to do this in one 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://training.qaonlinetraining.com/testPage.php")

driver.find_element(By.NAME,'name').send_keys("ITLearn")
driver.find_element(By.NAME,'email').send_keys("p@gmail.com")
driver.find_element(By.NAME,'website').send_keys("https://www.suryasangam.com/")
driver.find_element(By.NAME,'comment').send_keys("nice")
# driver.find_element(By.NAME,'submit').click()

#Radio Button
radioButton=driver.find_element(By.XPATH,'/html/body/form/input[4]')
radioButton.click()
if(radioButton.is_selected()):
    print("the test passed")
else:
    print("the test failed")
# driver.find_element(By.NAME,'submit').click()

#CheckBox
driver.find_element(By.NAME,'bike').click()
driver.find_element(By.NAME,'car').click()
driver.find_element(By.NAME,'boat').click()
driver.find_element(By.NAME,'horse').click()
# driver.find_element(By.NAME,'submit').click()

##DropDowns
    #single select
country=driver.find_element(By.NAME,'country')

selectCountry=Select(country)
selectCountry.select_by_visible_text("France")
# driver.find_element(By.NAME,'submit').click()
    #multiple select
skill=driver.find_element(By.NAME,'skill')
selectSkill=Select(skill)
selectSkill.select_by_value("qa")
selectSkill.select_by_value("prg")
selectSkill.select_by_value("db")
selectSkill.select_by_value("ba")
selectSkill.select_by_value("mgmt")
driver.find_element(By.NAME,'submit').click()

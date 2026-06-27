
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.get("https://training.qaonlinetraining.com/testPage.php")


#where you have only one choice
driver.find_element(By.ID,"alert").click()
alert1=driver.switch_to.alert
print(alert1.text)  #to print the text of the alert
alert1.accept()

# where youu have 2 choices
driver.find_element(By.ID,"confirm").click()
alert2=driver.switch_to.alert
print(alert2.text)  #to print the text of the alert

# to accept the alert

# alert2.accept()

#to cancle the alert

alert2.dismiss()


# where you have choice to pass value
driver.find_element(By.ID,"prompt").click()
alert3=driver.switch_to.alert
alert3.send_keys("PK")
print(alert3.text)  #to print the text of the alert
alert3.accept()

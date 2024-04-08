from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

lst=["anh xin lỗi","xin lỗi màaa"]

driver = webdriver.Chrome()
fb = "https://vi-vn.facebook.com/"
driver.get(fb)
email=driver.find_element(By.NAME,"email")
email.send_keys("cutdien123321456@gmail.com")
pw=driver.find_element(By.NAME,"pass")
pw.send_keys("baomat")
login=driver.find_element(By.NAME,"login")
sleep(3)
login.click()
sleep(3)
msg="https://web.facebook.com/messages/e2ee/t/7097160730321915"
driver.get(msg)
sleep(20)
for i in range(9):
	inpxpath="/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]/p"
	inp=driver.find_element(By.XPATH,inpxpath)
	inp.send_keys(random.choices(lst))
	inp.send_keys(Keys.RETURN)
	sleep(3)
#giờ thì ngồi đợi thôi
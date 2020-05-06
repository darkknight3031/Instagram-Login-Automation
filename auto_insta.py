import time
from selenium import webdriver


driver = webdriver.Chrome("__PATH__OF__WEBDRIVER__")

driver.get('https://www.instagram.com/')
time.sleep(3)
eid= driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
eid.send_keys('__USER_NAME__')

passcode= driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
passcode.send_keys('__USER_PASSWORD__')

log=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
log.click()
time.sleep(3)
noti=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
noti.click()
       


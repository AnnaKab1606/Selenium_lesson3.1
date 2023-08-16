import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button.click()

alert1 = browser.switch_to.alert
alert1.accept()


span1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = int(span1.text)
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input1.send_keys(y)


button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button.click()



# закрываем браузер после всех манипуляций
time.sleep(5)
browser.quit()
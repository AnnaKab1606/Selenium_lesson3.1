import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()

button1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button1.click()
time.sleep(2)

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = int(x.text)
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input1.send_keys(y)

button2 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
button2.click()

time.sleep(240)
browser.quit()
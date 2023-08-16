from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"   # прописываем адрес страницы сайта, с которым будем работать
browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element(By.XPATH, '//*[@id="book"]')   # находим элемент, на который потом нужно будет кликнуть
price_100 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), '$100'))    # говорим Selenium проверять в течение 12 секунд пока ена не станет 100
button1.click() # кликаем на кнопку

x = browser.find_element(By.XPATH, '//*[@id="input_value"]')   # находим элемент(число),которое получится в результате итога формулы функции
x = int(x.text)
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')  # находим поле для ввода текста
input1.send_keys(y)                                            # используется для ввода текста в текстовый элемент

button2 = browser.find_element(By.XPATH, '//*[@id="solve"]') # находим элемент
button2.click()                                              # кликаем на кнопку

time.sleep(240)
browser.quit()
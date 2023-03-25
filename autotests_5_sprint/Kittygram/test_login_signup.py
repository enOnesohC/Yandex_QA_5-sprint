from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#регистрируем новый акк
#нужно проверять текст сообщения

def test_login_signup():
    #Адрес сайта, который открываем
    link = "https://kittygram-frontend-7.prakticum-team.ru/signup"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)
    input1 = browser.find_element(By.ID, "1")
    input1.send_keys("123@gmail.com")

    time.sleep(1)
    input2 = browser.find_element(By.ID, "2")
    input2.send_keys("qwerty12345678")

    time.sleep(1)
    input2 = browser.find_element(By.ID, "3")
    input2.send_keys("qwerty12345678")

    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, "button-form_button__4mpE0 ")
    button.click()

    time.sleep(1)
    browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#авторизуемся
#идём на страницу добавления котоу
#идём на главную страницу

def test_add_to_main():
    #Адрес сайта, который открываем
    link = "https://kittygram-frontend-7.prakticum-team.ru/signin"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)
    input1 = browser.find_element(By.ID, "1")
    input1.send_keys("123@gmail.com")

    time.sleep(1)
    input2 = browser.find_element(By.ID, "2")
    input2.send_keys("qwerty12345678")

    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, "button-form_button__4mpE0.sign-in_btn__oC-J6")
    button.click()

    time.sleep(3)
    button1 = browser.find_element(By.CLASS_NAME, "button-header_icon__QsQzj")
    button1.click()

    #на странице добавления котоу

    time.sleep(3)
    button2 = browser.find_element(By.CLASS_NAME, "header_logo__wLirW")
    button2.click()

    time.sleep(3)
    browser.quit()

#test_add_to_main()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#авторизуемся
#добавляем нового кота

def test_add_new_cat():
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
    time.sleep(2)
    input3 = browser.find_element(By.XPATH, "//input[@name='name']")
    input3.send_keys("Murzik")

    time.sleep(1)
    input3 = browser.find_element(By.XPATH, "//input[@name='birth_year']")
    input3.send_keys("2000")

    time.sleep(3)
    button2 = browser.find_element(By.CLASS_NAME, "button-form_button__4mpE0.add-card-page_submit_btn__np9UM")
    button2.click()

    time.sleep(3)
    browser.quit()

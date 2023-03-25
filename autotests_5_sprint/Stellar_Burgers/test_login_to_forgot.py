from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_to_forgot():
    #Адрес сайта, который открываем
    link = "https://burger-frontend-7.prakticum-team.ru/login"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    button = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div[2]/a")
    button.click()
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.CLASS_NAME, "pb-6.text.text_type_main-medium")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Восстановление пароля" == welcome_text


    time.sleep(2)
    browser.quit()

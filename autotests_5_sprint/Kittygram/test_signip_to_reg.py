from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

#со страницы авторизации на страницу регистрации

def test_signip_to_reg():
    #Адрес сайта, который открываем
    link = "https://kittygram-frontend-7.prakticum-team.ru/signin"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, "text.text_type_medium-16.text_color_link.sign-in_nav__yZAbu")
    button.click()

    time.sleep(2)
    browser.quit()


#test_signip_to_reg()

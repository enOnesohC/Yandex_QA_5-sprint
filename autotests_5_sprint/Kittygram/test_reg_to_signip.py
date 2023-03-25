from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

#со страницы регистрации на страницу авторизации

def test_reg_to_signip():
    #Адрес сайта, который открываем
    link = "https://kittygram-frontend-7.prakticum-team.ru/signup"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, "text.text_type_medium-16.text_color_link.sign-up_nav__7NKpQ")
    button.click()

    time.sleep(2)
    browser.quit()

#test_reg_to_signip()

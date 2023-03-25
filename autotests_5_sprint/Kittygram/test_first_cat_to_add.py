from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#авторизуемся
#делаем нового кота
#изменяем нового кота
#надо ловить баги, что в поле год дичь получается

def test_first_cat_to_add():
    #Адрес сайта, который открываем
    link = "https://kittygram-frontend-7.prakticum-team.ru/signin"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(2)
    input1 = browser.find_element(By.ID, "1")
    input1.send_keys("123@gmail.com")

    time.sleep(1)
    input2 = browser.find_element(By.ID, "2")
    input2.send_keys("qwerty12345678")

    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, "button-form_button__4mpE0.sign-in_btn__oC-J6")
    button.click()

    time.sleep(2)
    button1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div[1]/article[1]/a/img")
    button1.click()

    time.sleep(2)
    button2 = browser.find_element(By.CLASS_NAME, "text.text_type_large.text_color_white.pl-8.button-header_text__1pP0C.false.button-header_hidden__Ay3Pt")
    button2.click()


    time.sleep(2)
    browser.quit()

#test_first_cat_to_add()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#авторизуемся
#делаем нового кота
#изменяем нового кота
#надо ловить баги, что в поле год дичь получается

def test_change_cat_logout():
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
    button1 = browser.find_element(By.CLASS_NAME, "button-header_icon__QsQzj")
    button1.click()

    #на странице добавления котоу
    time.sleep(2)
    input3 = browser.find_element(By.XPATH, "//input[@name='name']")
    input3.send_keys("Murzik")

    time.sleep(1)
    input3 = browser.find_element(By.XPATH, "//input[@name='birth_year']")
    input3.send_keys("2000")

    time.sleep(1)
    button2 = browser.find_element(By.CLASS_NAME, "button-form_button__4mpE0.add-card-page_submit_btn__np9UM")
    button2.click()

    # на странице нового кота
    time.sleep(2)
    button3 = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/article/div[1]/a")
    #button3 = browser.find_element(By.XPATH, "//button-header_button__gE5G7[@href='/cats/edit']")
    button3.click()

    #на странице редактирования котоу
    time.sleep(2)
    button4 = browser.find_element(By.XPATH, "/html/body/div[1]/div/header/div/button")
    button4.click()


    time.sleep(3)
    browser.quit()

#test_change_cat_logout()

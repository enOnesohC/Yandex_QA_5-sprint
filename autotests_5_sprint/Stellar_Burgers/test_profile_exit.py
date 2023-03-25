from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_profile_exit():
    #Адрес сайта, который открываем
    link = "https://burger-frontend-7.prakticum-team.ru/login"
    browser = webdriver.Chrome()
    browser.get(link)


    time.sleep(2)
    input1 = browser.find_element(By.XPATH, "//input[@name='email']")
    input1.send_keys("enonesohc@mail.ru")

    time.sleep(1)
    input2 = browser.find_element(By.XPATH, "//input[@name='password']")
    input2.send_keys("xCCuHfmBJyqV3Fv")

    time.sleep(1)
    button = browser.find_element(By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
    button.click()

    time.sleep(1)
    button1 = browser.find_element(By.CLASS_NAME, "app-header_link__2y8TU.app-header_link_position_last__3skWP")
    button1.click()

    time.sleep(1)
    button2 = browser.find_element(By.CLASS_NAME, "text.text_type_main-medium.text_color_inactive.pt-4.pb-4.profile-menu_button__10VBY")
    button2.click()

    time.sleep(2)
    browser.quit()

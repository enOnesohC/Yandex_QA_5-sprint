from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from seletools.actions import drag_and_drop
import time

def test_take_order():
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
    time.sleep(2)

    #browser.switch_to.frame(browser.find_element(By.CLASS_NAME, "main_main__tvROX"))
    #browser.switch_to.frame(0)
    #browser.switch_to.frame(0)

    #WebElement on which drag and drop operation needs to be performed
    fromElement = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/div/section[1]/div/div[1]/a[1]/img")
    #fromElement = browser.find_element(By.CLASS_NAME, "burger-ingredient_article__wQtAl")


    #WebElement to which the above object is dropped
    toElement = browser.find_element(By.CLASS_NAME, "burger-constructor_noBuns__3BH7a.false.burger-constructor_noBunsTop__w5Mru.ml-8.mb-4.mr-5.text.text_type_main-default")
    time.sleep(1)

    #так и не понял, почему из коробки drag_and_drop не работает, а сторонний работает
    drag_and_drop(browser, fromElement, toElement)
    #Creating object of Actions class to build composite actions
    #action = ActionChains(browser)
    #ActionChains(browser).drag_and_drop(fromElement, toElement).perform()
    #Building a drag and drop action and perform
    #action.drag_and_drop(fromElement, toElement).perform()
    #action.click_and_hold(fromElement).move_to_element(toElement).pause(2).release().perform()
    time.sleep(2)

    fromElement1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/main/div/section[1]/div/div[2]/a[1]")
    toElement1 = browser.find_element(By.CLASS_NAME, "burger-constructor_noBuns__3BH7a.false.ml-8.mb-4.mr-5.text.text_type_main-default")
    drag_and_drop(browser, fromElement1, toElement1)
    time.sleep(1)

    button1 = browser.find_element(By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")
    button1.click()
    time.sleep(20)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/p[1]")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "идентификатор заказа" == welcome_text

    browser.quit()

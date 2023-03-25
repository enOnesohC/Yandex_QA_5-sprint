import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="function")    # без этой штуки не запускается, фикстура, нужно изучать
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser    # финализатор, после выполнения теста инициализируется закрытие браузера
    print("\nquit browser..")
    browser.quit()

#страница входа для зарегистрированных пользователей
def go_to_signin_page(browser):
    link = "https://kittygram-frontend-7.prakticum-team.ru/signin"    # адрес
    browser.get(link)    # открытие адреса браузером
    time.sleep(1)    # ждём, чтобы точно перешло
#название тест, шобы pytest поймал
#def test_signin_page(browser):
#    go_to_signin_page(browser)

#страница входа для незарегистрированных пользователей
def go_to_signup_page(browser):
    link = "https://kittygram-frontend-7.prakticum-team.ru/signup"
    browser.get(link)
    time.sleep(1)
#название тест, шобы pytest поймал запуск теста
#def test_signup_page(browser):
#    go_to_signup_page(browser)

#вход на главную страницу из signin
def go_to_main_page_from_signin(browser):
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
    time.sleep(2)
# запуск теста
#def test_main_page_from_signin(browser):
#    go_to_main_page_from_signin(browser)

# вход на главную страницу из signup
#сейчас вызывает ошибку об уже существующем пользователе
# нужно делать произвольный логин через рандомайзер

#этот тест можно переименовать в поиск текста ошибки.
#если текст об ошибке есть, значит тест успешно пройден.
def go_to_main_page_from_signup(browser):
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
    time.sleep(2)

#def test_main_page_from_signup(browser):
#    go_to_main_page_from_signup(browser)

# добавляем нового кота через вход

def add_new_cat(browser):
    go_to_main_page_from_signin(browser)

    browser = webdriver.Chrome()

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

    time.sleep(1)
    button2 = browser.find_element(By.CLASS_NAME, "button-form_button__4mpE0.add-card-page_submit_btn__np9UM")
    button2.click()
    time.sleep(2)

def test_add_new_cat(browser):
    add_new_cat(browser)

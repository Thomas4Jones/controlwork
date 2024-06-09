import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import *
from config.config import SeleniumAction
from contrtest.contr_locator import *
from contrtest.contr_data import *
from selenium.webdriver.firefox.service import Service
from config.action import SeleniumAction
import os


@pytest.fixture
def browser():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    gecko_path = os.path.join(current_dir, "geckodriver.exe")
    web_service = Service(gecko_path)
    driver = webdriver.Firefox(service=web_service)
    driver.get(data_page)
    yield driver
    driver.quit()


@pytest.fixture
def selenium_action(browser):
    selenium_action = SeleniumAction(browser)
    yield selenium_action


@pytest.fixture
def login(browser, selenium_action):
    def login_function():
        browser.get(data_page)
        assert selenium_action.action_get_text(locator_text_loginpage) == data_text
        selenium_action.action_fill_input(locator_username, data_username)
        selenium_action.action_fill_input(locator_password, data_password)
        selenium_action.action_click_element(locator_button_login)
        selenium_action.action_wait_on_page(3000)
        assert "https://the-internet.herokuapp.com/secure" in browser.current_url.lower()
        print('Вход успешный')
    yield login_function


@pytest.fixture
def logout(browser, selenium_action):
    def logout_function():
        selenium_action.action_click_element(locator_button_logout)
        selenium_action.action_wait_on_page(3000)
        assert "https://the-internet.herokuapp.com/login" in browser.current_url.lower()
        print('Выход успешный')
    yield logout_function


@pytest.fixture
def login1(browser, selenium_action):
    def login1_function():
        browser.get(data_page)
        assert selenium_action.action_get_text(locator_text_loginpage) == data_text
        selenium_action.action_fill_input(locator_username, data_username)
        selenium_action.action_click_element(locator_button_login)
        selenium_action.action_wait_on_page(3000)
        assert "https://the-internet.herokuapp.com/login" in browser.current_url.lower()
        print('Входа нет')
    yield login1_function


@pytest.fixture
def login2(browser, selenium_action):
    def login2_function():
        browser.get(data_page)
        assert selenium_action.action_get_text(locator_text_loginpage) == data_text
        selenium_action.action_fill_input(locator_username, data_notusername)
        selenium_action.action_fill_input(locator_password, data_notpassword)
        selenium_action.action_click_element(locator_button_login)
        selenium_action.action_wait_on_page(3000)
        assert "https://the-internet.herokuapp.com/login" in browser.current_url.lower()
        print('Входа нет')
    yield login2_function

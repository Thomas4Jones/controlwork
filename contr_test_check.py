from contrtest.contr_test_step import *


@pytest.mark.smoke_market
def test_loginpage_successful_(selenium_action, login, logout):
    """Проверка входа и выхода"""
    login()
    logout()
    print('Тест успешный')
    selenium_action.action_close_current_window()


@pytest.mark.smoke_market
def test_loginpage_odnopole(selenium_action, login1):
    """Проверка входа при заполнении одного поля"""
    login1()
    print('Тест успешный')
    selenium_action.action_close_current_window()


@pytest.mark.smoke_market
def test_loginpage_unsuccessful(selenium_action, login2):
    """Проверка входа при заполнении неправильных логина и пароля """
    login2()
    print('Тест успешный')
    selenium_action.action_close_current_window()

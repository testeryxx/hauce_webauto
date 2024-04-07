import pytest

from VAR.DSW_VAR import *
from datadriver.yamldriver import load_yaml
from logic.login import LoginPage


@pytest.mark.parametrize('data', load_yaml())
def test_login(browser, data):
    login = LoginPage(browser)
    login.login(LOGIN_URL, USERNAME, PWD)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from kewwords.keyword import WebKeys
from locate.loginpage import *


class LoginPage(WebKeys):
    '''登录操作'''

    def login(self, url, username, pwd):
        self.open_url(url)

        # 实例化wait
        wait = WebDriverWait(self.driver, 5)

        # 根据登录读书屋作为等待条件
        wait.until(ec.text_to_be_present_in_element((By.XPATH, "//h3"), "登陆读书屋"))

        # 登录操作
        self.locator(*login_user).send_keys(username)
        self.locator(*login_pwd).send_keys(pwd)
        self.locator(*login_btn).click()

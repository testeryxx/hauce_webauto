# -*- coding:utf-8 -*-
import allure


@allure.epic("读书屋项目")
@allure.feature("读书屋 - 登录模块")
@allure.story("登录流程用例：流程00")
class TestHome:

    @allure.step("步骤一：打开项目的url地址")
    def step01(self, browser):
        browser.get("http://120.25.127.201:18001/user/login.html")

    @allure.step("步骤二：输入账号")
    def step02(self, browser):
        browser.find_element('id', 'txtUName').send_keys('17798989898')

    @allure.step("步骤三：输入密码")
    def step03(self, browser):
        browser.find_element('id', 'txtPassword').send_keys('123456')

    @allure.step("步骤四：点击登录")
    def step04(self, browser):
        browser.find_element('id', 'btnLogin').click()

    @allure.title("登录用例：test_case_01")
    @allure.story("登录流程用例：流程01")
    def test_case_01(self, browser):
        print("这个是 test_case_01 测试用例")
        print(f"browser: {browser}")
        self.step01(browser)
        self.step02(browser)
        self.step03(browser)
        self.step04(browser)

    @allure.title("注册用例：test_case_02")
    def test_case_02(self, browser):
        print("这个是 test_case_02 测试用例")

    @allure.title("首页用例：test_case_03")
    def test_case_03(self, browser):
        print("这个是 test_case_03 测试用例")

import pytest, allure
from selenium import webdriver


@pytest.fixture()
def browser():
    # 用例前置操作
    global driver
    driver = webdriver.Chrome()
    yield driver
    # 用例后置操作,用例执行完毕，关闭浏览器
    driver.quit()


"""
用例的失败截图
1.在上课的了解一下基本的逻辑
2.能够在面试中稍微的说几句这个里面的逻辑
3.工作中，直接复制粘贴
"""


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    # 获取测试用例的执行结果对象
    out = yield

    """
        从result对象out获取调用结果的测试报告，返回一个report对象

        report对象的属性：
        包含三个属性：
        when: setup、call、teardown三个值
        nodeid: 测试用例的名称
        outcome: 测试用例的执行结果 passed、failed
    """
    report = out.get_result()  # 返回一个report对象

    # 根据判断条件来进行截图取证
    if report.when == 'call':  # 仅仅只获取用例call阶段的执行结果
        # 获取用例call执行结果为失败的情况：
        xfail = hasattr(report, 'wasxfail')  # hasattr方法会：返回对象是否具有给定的名称的属性

        # 如果测试用例被跳过并且标记为预期失败，或者测试用例执行失败并且不是预期失败
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 添加allure报告截图
            with allure.step("添加失败截图... ..."):
                # 使用allure自带的添加附件的方法
                allure.attach(driver.get_screenshot_as_png(), '失败截图', allure.attachment_type.PNG)

        # 成功用例的截图操作
        elif report.passed:
            # 如果测试用例执行通过，添加allure报告截图
            with allure.step("添加成功截图... ..."):
                # 使用allure自带的添加附件的方法
                allure.attach(driver.get_screenshot_as_png(), '成功截图', allure.attachment_type.PNG)

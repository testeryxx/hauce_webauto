# -*- coding:utf-8 -*-
import pytest, os

if __name__ == '__main__':
    pytest.main(['-s', '--alluredir', './result', '--clean-alluredir'])  # 会收集测试用例执行的数据，存放到alluredir下面
    os.system('allure generate ./result -o ./report --clean')

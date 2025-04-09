# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""登录功能测试模块 - 使用fixture管理driver"""

import os
import pytest
import logging
import allure
from utils.excel_utils import ReadExcel
from utils.path_utils import paths
from test.pages.loginPage import LoginPage

log = logging.getLogger(__name__)


def get_cases():
    """获取测试数据"""
    path = paths.data / "UItestdata.xlsx"
    sheet_name = 'Login'
    cols = list(range(5))
    read_excel = ReadExcel(path, sheet_name, usecols=cols)
    return read_excel.to_list()


# login_page fixture现在依赖于driver，并且会跟随driver的scope设置
@pytest.fixture
def login_page(driver):
    """创建LoginPage实例的fixture"""
    page = LoginPage(driver)
    # 初始化时打开登录页面
    page.open(f"file://{paths.html}/loginpage.html")
    return page


class TestLogin:
    """登录测试类"""

    @allure.title('登录测试')
    @pytest.mark.parametrize('case_id, case_name, username, password, expected_message', get_cases())
    def test_login(self, login_page, case_id, case_name, username, password, expected_message):
        """登录功能测试用例"""
        log.info(f"{case_id}--->{case_name}--->{expected_message}")

        # 每次测试前刷新页面，确保测试状态干净
        login_page.refresh()

        # 执行登录测试
        actual_message = login_page.login(username, password)
        assert actual_message == expected_message


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='登录测试')
    parser.add_argument('--report', action='store_true', help='生成Allure报告')
    args = parser.parse_args()

    if args.report:
        pytest.main(['-s', '-q', 'test_01_login.py', '--clean-alluredir', '--alluredir=allure-results'])
        os.system("allure generate -c -o allure-report")
    else:
        pytest.main(['-vs', 'test_01_login.py'])
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# """LoginPage: 登录页面操作封装"""
#
# import time
# from selenium.webdriver.common.by import By
# from test.pages.basePage import BasePage
# from utils.path_utils import paths
#
#
# class LoginPage(BasePage):
#     # 定义页面元素的定位器
#     LOCATORS = {
#         'username': (By.XPATH, "//*[@id='username']"),
#         'password': (By.XPATH, "//*[@id='password']"),
#         'login_btn': (By.XPATH, "//*[@id='loginForm']/input[3]"),
#         'message': (By.XPATH, "//*[@id='message']")
#     }
#
#     def __init__(self, driver=None):
#         super().__init__(driver)
#         self.login_url = f"file://{paths.html}/loginpage.html"
#
#     def login(self, username=None, password=None):
#         self.open(self.login_url)
#         self.input(*self.LOCATORS['username'], username or '')
#         self.input(*self.LOCATORS['password'], password or '')
#         self.click(*self.LOCATORS['login_btn'])
#         time.sleep(2)
#         return self.text(*self.LOCATORS['message'])
#
#
# if __name__ == '__main__':
#     with LoginPage() as page:
#         message = page.login('test', 'abcd1234')
#         print(f"登录结果: {message}")

# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""LoginPage: 登录页面操作封装"""

import time
from selenium.webdriver.common.by import By
from test.pages.basePage import BasePage
from utils.path_utils import paths


class LoginPage(BasePage):
    # 定义页面元素的定位器
    LOCATORS = {
        'username': (By.XPATH, "//*[@id='username']"),
        'password': (By.XPATH, "//*[@id='password']"),
        'login_btn': (By.XPATH, "//*[@id='loginForm']/input[3]"),
        'message': (By.XPATH, "//*[@id='message']")
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.login_url = f"file://{paths.html}/loginpage.html"

    def login(self, username=None, password=None):
        """
        执行登录操作
        注意：如果已经在测试中打开了页面，这里不会重新打开页面
        """
        # 简化登录方法，不再重复打开页面，因为fixture会处理
        # 只输入用户名和密码，然后点击登录
        self.input(*self.LOCATORS['username'], username or '')
        self.input(*self.LOCATORS['password'], password or '')
        self.click(*self.LOCATORS['login_btn'])
        time.sleep(2)
        return self.text(*self.LOCATORS['message'])
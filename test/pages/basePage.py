#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""BasePage: 封装Selenium基础操作"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver=None, timeout=10):
        self.driver = driver or webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        self.find(by, value).click()

    def input(self, by, value, text):
        elem = self.find(by, value)
        elem.clear()
        elem.send_keys(text)

    def text(self, by, value):
        return self.find(by, value).text

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()


if __name__ == '__main__':
    from utils.path_utils import paths

    url = f"file://{paths.html/'loginpage.html'}"

    with BasePage() as page:
        page.open(url)
        page.input(By.ID, "username", "test")
        page.input(By.ID, "password", "abcd1234")
        page.click(By.XPATH, "//*[@id='loginForm']/input[3]")
        print(page.text(By.ID, "message"))
        time.sleep(3)
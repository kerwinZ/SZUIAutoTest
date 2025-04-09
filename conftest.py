# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# """Pytest配置：失败截图和其他钩子函数"""
#
# import os
# from pathlib import Path
# from datetime import datetime
# import pytest
#
#
# def _get_driver_from_item(item):
#     # 尝试从fixture获取driver
#     driver = item.funcargs.get("driver")
#
#     # 如果没有，尝试从测试类实例获取
#     if not driver and hasattr(item, "instance"):
#         instance = item.instance
#         if hasattr(instance, "page") and hasattr(instance.page, "driver"):
#             driver = instance.page.driver
#
#     return driver
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#
#     if report.when == "call" and report.failed:
#         driver = _get_driver_from_item(item)
#
#         if driver:
#             # 创建截图目录
#             screenshots_dir = Path("screenshots")
#             screenshots_dir.mkdir(exist_ok=True)
#
#             # 生成文件名
#             now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#             filename = screenshots_dir / f"{item.name}_{now}.png"
#
#             # 保存截图
#             driver.save_screenshot(str(filename))
#
#             # 尝试添加到Allure报告
#             try:
#                 import allure
#                 allure.attach(
#                     driver.get_screenshot_as_png(),
#                     name=f"{item.name}_{now}",
#                     attachment_type=allure.attachment_type.PNG
#                 )
#             except (ImportError, AttributeError):
#                 pass
#
#             print(f"\n[pytest] 失败截图保存至：{filename}")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pytest配置：提供driver fixture和失败截图功能"""

import os
from pathlib import Path
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 直接设置driver fixture的作用域为session
@pytest.fixture(scope="session")
def driver():
    """
    提供WebDriver实例的fixture，作用域为session
    整个测试会话期间只使用一个浏览器实例
    """
    # 创建WebDriver选项
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # 无头模式，取消注释以启用

    # 创建driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # 提供driver给测试
    yield driver

    # 测试结束后自动清理
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """测试报告钩子，用于处理失败截图"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # 直接从fixture获取driver
        driver = item.funcargs.get("driver")

        if driver:
            # 创建截图目录
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            # 生成文件名
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = screenshots_dir / f"{item.name}_{now}.png"

            # 保存截图
            driver.save_screenshot(str(filename))

            # 尝试添加到Allure报告
            try:
                import allure
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"{item.name}_{now}",
                    attachment_type=allure.attachment_type.PNG
                )
            except (ImportError, AttributeError):
                pass

            print(f"\n[pytest] 失败截图保存至：{filename}")
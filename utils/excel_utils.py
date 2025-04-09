#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Excel文件读取工具"""

import pandas as pd
from pathlib import Path


class ReadExcel:
    """读取Excel数据并进行处理"""

    def __init__(self, path, sheet_name, usecols=None):
        self.path = Path(path)
        self.sheet_name = sheet_name
        self.usecols = usecols
        self._df = None  # 懒加载缓存

    def _load_data(self):
        """懒加载读取Excel，避免重复读取"""
        if self._df is None:
            try:
                self._df = pd.read_excel(
                    self.path,
                    sheet_name=self.sheet_name,
                    usecols=self.usecols
                )
            except Exception as e:
                print(f"读取Excel失败: {e}")
                self._df = pd.DataFrame()
        return self._df

    def get_clean_data(self):
        """返回填充空值后的数据"""
        return self._load_data().fillna('')

    def to_list(self):
        """将每一行转换为列表"""
        return self.get_clean_data().values.tolist()


if __name__ == '__main__':
    from path_utils import paths

    path = paths.data / "UItestdata.xlsx"
    sheet_name = 'Login'
    usecols = list(range(5))

    reader = ReadExcel(path, sheet_name, usecols)
    print(reader.to_list())
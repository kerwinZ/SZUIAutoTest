#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""项目路径管理工具"""

from pathlib import Path


class Paths:
    """项目路径管理器，支持点语法访问"""

    def __init__(self, subdirs):
        self.root = Path(__file__).resolve().parent.parent
        for name in subdirs:
            path = self.root / name
            if not path.exists():
                print(f"提示：目录不存在：{path}")
            setattr(self, name, path)

    def __getitem__(self, key):
        """支持字典式访问"""
        return getattr(self, key, None)


# 所有子目录名
_subdirs = ['config', 'data', 'html', 'log', 'utils', 'test']

# 创建路径管理器实例
paths = Paths(_subdirs)


if __name__ == '__main__':
    print(f"项目根目录: {paths.root}")
    print(f"配置目录: {paths.config}")
    print(f"数据目录: {paths.data}")
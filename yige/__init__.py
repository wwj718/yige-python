# -*- coding: utf-8 -*-

"""
yige
~~~~~~~~~~~~~~~~
This module provides a yige.ai classes to manage requests.
"""

__author__ = """wenjiewu"""
__email__ = 'wuwenjie718@gmail.com'
__version__ = '0.2.0'
__contributors__ = []
__license__ = "MIT"
from .yige import Yige
from .yige_action import ActionHandle,run_action
# 使用相对路径引用内部模块，对外暴露
# https://github.com/api-ai/api-ai-python/blob/master/apiai/__init__.py

# 对外暴露
__all__ = ['Yige','ActionHandle','run_action']


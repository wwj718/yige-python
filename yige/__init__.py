# -*- coding: utf-8 -*-

"""
yige
~~~~~~~~~~~~~~~~
This module provides a yige.ai classes to manage requests.
"""

__author__ = """wenjiewu"""
__email__ = 'wuwenjie718@gmail.com'
__version__ = '0.1.0'
__contributors__ = []
__license__ = "MIT"
from .yige import Yige
# 使用相对路径引用内部模块，对外暴露
# https://github.com/api-ai/api-ai-python/blob/master/apiai/__init__.py

# 对外暴露
__all__ = ['Yige']

# -*- coding: utf-8 -*-
# @Time: 2019/5/20 19:42
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: SimpleLinkedList.py
# @Software: PyCharm


class SimpleLinkedList(object):
    def __init__(self, data, next_data = None):
        """
        初始化链表
        :param data:
        :param next_data: 避免与`python`已有`next`函数重名
        """
        self.data = data
        self.next_data = next_data

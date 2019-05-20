# -*- coding: utf-8 -*-
# @Time: 2019/5/20 19:42
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: LinkedList.py
# @Software: PyCharm


class LinkedList(object):
    def __init__(self, data, Next = None):
        """
        初始化链表
        :param data:
        :param Next:
        """
        self.data = data
        self.next = next

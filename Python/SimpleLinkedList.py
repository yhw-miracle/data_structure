# -*- coding: utf-8 -*-
# @Time: 2019/5/20 19:42
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: SimpleLinkedList.py
# @Software: PyCharm


class SimpleLinkedList(object):
    """
    1.单链表反转
    2.链表中环的检测
    3.两个有序链表合并
    4.删除链表倒数第n个节点
    5.求链表的中间节点
    """
    def __init__(self, data, next_data = None):
        """
        初始化链表
        :param data:
        :param next_data: 避免与`python`已有`next`函数重名
        """
        self.data = data
        self.next_data = next_data

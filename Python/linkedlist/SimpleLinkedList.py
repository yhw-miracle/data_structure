# -*- coding: utf-8 -*-
# @Time: 2019/5/20 19:42
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: SimpleLinkedList.py
# @Software: PyCharm


class SimpleLinkedList(object):
    """
    单链表
    """
    def __init__(self, data, next_data = None):
        """
        初始化链表
        :param data:
        :param next_data: 避免与`python`已有`next`函数重名
        """
        self.data = data
        self.next_data = next_data

    def reverse(self):
        """
        单链表反转
        :return:
        """
        pass

    def is_cycle(self):
        """
        链表中环的检测
        :return:
        """
        pass

    def union(self):
        """
        两个有序链表合并
        :return:
        """
        pass

    def delete_by_back_index(self):
        """
        删除链表倒数第n个节点
        :return:
        """
        pass

    def middle_node(self):
        """
        求链表的中间节点
        :return:
        """
        pass

if __name__ == '__main__':
    pass

# -*- coding: utf-8 -*-
# @Time: 2019/7/18 21:06
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo001_search.py
# @Software: PyCharm
import random


def single_search():
    """
    简单查询
    :return:
    """


def binary_search():
    """
    二分查找
    :return:
    """


def get_random_data_list(length):
    """
    随机测试数据
    :param length: 测试数据长度
    :return: 测试数据列表
    """
    data_list = []
    for _ in range(length):
        data_list.append(random.randint(1, 100))
    return data_list


if __name__ == '__main__':
    data_list = []

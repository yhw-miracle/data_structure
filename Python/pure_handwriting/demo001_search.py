# -*- coding: utf-8 -*-
# @Time: 2019/7/18 21:06
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo001_search.py
# @Software: PyCharm
import random


def single_search(data_list, value):
    """
    简单查询
    :param data_list: 查询数据列表，如：[1, 20, 23, 32, 21]
    :param value: 查询值，如：32
    :return: 查询结果，如，"data-list: 3 ---> 32"
    """
    i = 1
    for v in data_list:
        if v == value:
            return "data_list: {} ---> {}".format(i, value)
        i += 1
    return "data_list no {}".format(value)


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
    data_list = get_random_data_list(30)
    print(data_list)

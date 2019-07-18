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


def binary_search(data_list, value):
    """
    二分查找
    :param data_list: 查询数据列表，如：[1, 20, 23, 32, 21]
    :param value: 查询值，如：32
    :return: 查询结果，如，"data-list: 3 ---> 32"
    """
    low = 0
    high = data_list.length - 1
    data_list = sorted(data_list)

    while low <= high:
        mid = (low + high) / 2
        if data_list[mid] < value:
            low = mid + 1
        elif data_list[mid] > value:
            low = mid -1
        elif data_list[mid] == value:
            return "data_list: {} ---> {}".format(data_list.index(value), value)


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
    print(single_search(data_list, 23))
    print(single_search(data_list, 12))

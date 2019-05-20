# -*- coding: utf-8 -*-
# @Time: 2019/5/20 19:06
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: array.py
# @Software: PyCharm


# 数组
class Array(object):
    def __init__(self):
        """
        初始化数组
        """
        self.data = []
        self.length = len(self.data)

    def insert(self, x, index = 0):
        """
        给数组指定位置插入数据
        :param index: 待插入位置
        :param x: 待插入的数据
        :return:
        """
        if index < 0 or index >= self.length:
            return "插入失败"
        else:
            self.data.insert(index, x)
            self.length += 1

    def modify(self, x, index):
        """
        修改数组指定位置的数据
        :param index: 待修改的位置
        :param x: 待修改的新值
        :return:
        """
        if index < 0 or index >= self.length:
            return "下标 %d 错误" % index
        else:
            self.data.pop(index)
            self.data.insert(index, x)

    def delete(self, index):
        """
        删除数组指定位置的元素
        :param index:
        :return:
        """
        if index < 0 or index >= self.length:
            return "下标 %d 错误" % index
        else:
            self.data.pop(index)
            self.length -= 1

    def print_array(self):
        """
        打印数组元素
        :return:
        """
        for i in self.data:
            print(i,",")


if __name__ == '__main__':
    array = Array()
    array.insert(1)
    array.insert(2)
    array.insert(3)
    array.insert(4)
    array.insert(5)
    array.print_array()

    array.modify(7, 2)
    array.print_array()

    array.delete(0)
    array.print_array()

    print(array.length)

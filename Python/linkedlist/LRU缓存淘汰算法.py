# -*- coding: utf-8 -*-
# @Time: 2019/5/23 20:43
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: LRU缓存淘汰算法.py
# @Software: PyCharm

"""
实现`LRU`缓存淘汰算法
    1. 维护一个有序单链表。
    2. 访问的数据在链表中，删除该元素结点。
    3. 访问的数据不在链表中，
        若缓存未满，将该结点插入到表头；
        若缓存已满，删除表尾的结点，并将结点插入到表头。
"""

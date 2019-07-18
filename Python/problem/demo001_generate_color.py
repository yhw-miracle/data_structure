# -*- coding: utf-8 -*-
# @Time: 2019/7/18 20:04
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo001_generate_color.py
# @Software: PyCharm
import string


def generate_color_way01():
    """
    生成所有六位`RGB`颜色，复杂度为：O(n^6)，不可取
    :return:
    """
    all_ch = string.digits + string.ascii_uppercase[0:6]
    print(all_ch)

    color_list = []
    for ch1 in all_ch:
        for ch2 in all_ch:
            for ch3 in all_ch:
                for ch4 in all_ch:
                    for ch5 in all_ch:
                        for ch6 in all_ch:
                            color_list.append(ch1 + ch2 + ch3 + ch4 + ch5 + ch6)

    return color_list


if __name__ == '__main__':
    pass

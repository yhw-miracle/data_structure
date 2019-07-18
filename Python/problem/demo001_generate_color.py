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


def dec2hex(num):
    """
    十进制转换十六进制
    16(D) ---> 10(H)
        16/16=1......0
        1/16=0......1
    :param num:
    :return:
    """
    base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
    hex_list = []
    if num < 0:
        return '-' + dec2hex(abs(num))
    while True:
        num,rem = divmod(num, 16)
        hex_list.append(base[rem])
        if num == 0:
            return ''.join(hex_list[::-1])


def generate_color_way02():
    """
    1. 生成`R`、`G`、`B`三组值，其值范围是`0~255`，十进制数;
    2. 将十进制数转为十六进制数
    时间复杂度为`O(n^3)`，但是在进行十进制数转换为十六进制数时，很耗时，故也是好的方法
    :return:
    """
    rgb_dec_list = []
    rgb_hex_list = []

    for r in range(255):
        for g in range(255):
            for b in range(255):
                print(r, g, b)
                rgb_dec_list.append((r, g, b))
                # color_hex_one = str(dec2hex(r)) + str(dec2hex(g)) + str(dec2hex(b))
                # print(color_hex_one)
                # rgb_hex_list.append(color_hex_one)

    return rgb_hex_list


if __name__ == '__main__':
    pass

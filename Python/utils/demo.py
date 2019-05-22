# -*- coding: utf-8 -*-
# @Time: 2019/5/21 13:45
# @Author: yhw-miracle
# @Email: yhw_software@qq.com
# @File: demo.py
# @Software: PyCharm

import datetime


if __name__ == '__main__':
    with open("../../everyday_task/" + str(datetime.date.today()) + ".md", "w") as file:
        file.write("> Continue learning...\n\n")

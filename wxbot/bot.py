# coding=utf-8
# 需要python3

from wxpy import *

bot = Bot(console_qr=2)


def check_duplicate(key):
    groups = bot.groups().search(key)

    check_list = []

    def check_exist(group_one, group_two):
        print(group_one, group_two)

        for t in check_list:
            if group_one in t and group_two in t:
                return
            else:
                check_list.append((group_one, group_two))

        if not check_list:
            check_list.append((group_one, group_two))

    for _g in groups:
        print(_g)
        for _p in groups:
            if not _g == _p:
                check_exist(_g, _p)

    for g1, g2 in check_list:
        print(g1, g2)
        for _m in g1.members:
            for _n in g2.members:
                if _m == _n:
                    print(g1.name, ',', g2.name, ',', _m.display_name, ',', _n.display_name, ',', _n.nick_name)


embed()

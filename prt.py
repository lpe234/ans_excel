# -*- coding: utf-8 -*-

__author__ = 'lpe234'
__date__ = '2014-11-30'


def do_print(num):
    for x in range(1, num+1):
        line = range(1, x+1)
        line.extend(sorted(line[:-1], reverse=True))
        print '  '*(num-x) + ' '.join(str(x) for x in line)


def sorted_key(obj):
    sorted_list = ['邹成', '刘强', '段方方', '臧中林', '徐小波', '刘晓涵', '刘承林', '徐标', '刘玉印', '熊保健',\
                   '郑绍军', '王志鹏', '游恒耀', '林子华', '戚娜', '周峥巍', '张宁', 'Piyush', 'Srinivas',\
                   'Santhosh', '周兴平', '郭键',\
                   '姚殊技', '张婷婷', '李皎', '秦欢', '姜铨', '陈洋',\
                   '戴翔', '唐培', '周启龙', '刘文涛',\
                   '张全政', '徐志远',\
                   '李亮', '彭阳', '谭宇', '刘易东',\
                   '曲晓欢', '唐亚琴',\
                   '王路军',]
    return sorted_list.index(obj)


if __name__ == '__main__':
    # do_print(5)
    sorted_key()
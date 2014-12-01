# -*- coding: utf-8 -*-

__author__ = 'lpe234'
__date__ = '2014-11-29'

import xlrd
import datetime

# Excel文件名称
# file_name = 'sp.xls'
file_name = 'sp_2.xls'

# 读取Excel文件中所有数据
data = xlrd.open_workbook(file_name)

# 读取Excel文件在的 第一个工作表
sheet = data.sheets()[0]

# 工作表行、列总数
rows = sheet.nrows
cols = sheet.ncols

# 初始化 数据存储用字典
data_dict = {}
data_list = []


# 自定义， 排序序列
def sorted_key(obj):
    # 保留列表 首位置 用来排序，未出现在列表中的姓名
    sorted_list_2 = [u'', u'邹成', u'刘强', u'段方方', u'臧中林', u'徐小波', u'刘晓涵', u'刘承林', u'徐标', u'刘玉印', u'熊保健', u'郑绍军', u'王志鹏', u'游恒耀', u'林子华', u'戚娜', u'周峥巍', u'张宁', u'Piyush', u'srinivas', u'Santhosh', u'周兴平', u'郭键', u'姚殊技', u'张婷婷', u'李皎', u'秦欢', u'姜铨', u'陈洋', u'戴翔', u'唐培', u'周启龙', u'l刘文涛', u'张全政', u'徐志远', u'李亮', u'彭阳', u'谭宇', u'刘易东', u'曲晓欢', u'唐亚琴', u'陈明', u'王路军',]
    if obj[0] in sorted_list_2:
        return sorted_list_2.index(obj[0]), obj[1], obj[2], obj[3]
    else:
        return 0

for index in range(rows):
    # 依次读取excel的每行数据
    line = sheet.row_values(index)
    # 排除“委托”情况，第一行数值为 “13000825”时，
    if line[0] == 13000825:
        # 读取该行 姓名
        # name = line[3].encode('utf-8')
        name = line[3]
        # 读取该行 日期，星期
        datetime_tuple = xlrd.xldate_as_tuple(line[7], 0)
        date = datetime.date(datetime_tuple[0], datetime_tuple[1], datetime_tuple[2])
        weekday = date.weekday() + 1
        # 读取该行 持续时间
        duration = int(line[9])

        # 构造每行数据
        data_line = [name, date, weekday, duration]
        # 将每行处理后的数据，添加到数据总表
        data_list.append(data_line)

# 修正数据，对数据按 姓名-> 时间 -> 星期 -> 持续时间 (升序) 进行排列
fixted_data_list = sorted(data_list, key=sorted_key)


#  诚信
def do_print(x):
    return ' '.join([x[0].encode('utf-8'), str(x[1]), str(x[2]), str(x[3])])

xx_list = []
temp_duration = None
for data_line in fixted_data_list:
    if xx_list:
        if xx_list[-1][:-1] == data_line[:-1]:
            # print do_print(data_line), '###########33'
            # print data_line[-1]
            # 持续时间，总和
            temp_duration = xx_list[-1][-1] + data_line[-1]
            xx_list[-1][-1] = temp_duration
            # print temp_duration
            continue
    xx_list.append(data_line)
    # print do_print(data_line)

# for x in fixted_data_list:
f = open('sp_2_2.txt', 'a+')
for x in xx_list:
    data_line = [x[0].encode('utf-8'), str(x[1]), str(x[2]), str(x[3])]
    print ' '.join(data_line)
    f.write(' '.join(data_line))
    f.write('\n')
f.close()

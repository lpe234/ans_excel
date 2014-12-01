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
    # sorted_list_1 = ['', '邹成', '刘强', '段方方', '臧中林', '徐小波', '刘晓涵', '刘承林', '徐标', '刘玉印', '熊保健', '郑绍军', '王志鹏', '游恒耀', '林子华', '戚娜', '周峥巍', '张宁', 'Piyush', 'Srinivas', 'Santhosh', '周兴平', '郭键', '姚殊技', '张婷婷', '李皎', '秦欢', '姜铨', '陈洋', '戴翔', '唐培', '周启龙', 'l刘文涛', '张全政', '徐志远', '李亮', '彭阳', '谭宇', '刘易东', '曲晓欢', '唐亚琴', '王路军']
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

# fixted_data_dict = {}
# for x in fixted_data_list:
#     if x[0] in fixted_data_dict:
#         if x[1] in fixted_data_dict[x[0]]:
#             fixted_data_dict[x[0]][x[1]].append(x[3])
#         else:
#             fixted_data_dict[x[0]][x[1]] = [x[3], ]
#     else:
#         fixted_data_dict[x[0]] = {}
# print fixted_data_dict

f = open('sp_2.txt', 'a+')
for x in fixted_data_list:
    # print x[0], x[1], x[2], x[3]
    # f.write(' '.join([str(val) for val in x]))
    data_line = [x[0].encode('utf-8'), str(x[1]), str(x[2]), str(x[3])]
    print ' '.join(data_line)
    f.write(' '.join(data_line))
    f.write('\n')
f.close()






# data_dict_2 = {}
# sort_key = {}
# for date, data_lines in data_dict.items():
#     print '#############'*10
#     print date, data_lines[0][2]
#     data_lines.sort(key=lambda x: x[0])
#     for data_line in data_lines:
#         print data_line[0]




# -*- coding: utf-8 -*-


data_list = ['a 2014-11-03 1 10',
             'a 2014-11-05 3 20',
             'a 2014-11-05 3 20',
             'a 2014-11-05 3 20',
             'a 2014-11-06 4 20',
             'a 2014-11-09 7 10',
             'a 2014-11-10 1 20',
             'a 2014-11-11 2 10',
             'a 2014-11-11 2 10',
             'a 2014-11-14 5 10',
             'a 2014-11-16 7 10',
             'a 2014-11-17 1 10',
             'b 2014-11-18 2 10',
             'b 2014-11-19 3 20',
             'b 2014-11-20 4 10',
             'b 2014-11-20 4 20',
             'b 2014-11-21 5 20',
             'b 2014-11-22 6 20',
             'b 2014-11-24 1 20', ]

new_data_list = []

data_list_len = len(data_list)


for i_1 in range(len(data_list)):
    i_2 = i_1
    while 1:
        i_2 += 1
        try:
            data_1 = data_list[i_1].split()
            data_2 = data_list[i_2].split()
            if data_1[:-1] == data_2[:-1]:
                data_1[3] = str(int(data_1[3]) + int(data_2[3]))
                print data_1, '#######'
                del data_list[i_2]
            else:
                break
        except(IndexError, ):
            break
    i_1 = i_2


for x in data_list:
    print x


























# for index in range(len(data_list)):
#     try:
#         old_line = data_list[index].split()
#
#         index += 1
#         new_line = data_list[index].split()
#         if (old_line[0] == new_line[0]) and (old_line[1] == new_line[1]):
#             old_line[3] = str(int(old_line[3]) + int(new_line[3]))
#             fixed_line = ' '.join(old_line)
#             data_list[index] = fixed_line
#
#             del data_list[index]
#     except(IndexError, ):
#         continue
#
# for x in data_list:
#     print x
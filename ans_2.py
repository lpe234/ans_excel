# -*- coding: utf-8 -*-

__author__ = 'lpe234'
__date__ = '2014-11-30'

file_name = 'sp_2.txt'
f = open(file_name, 'r')

for line in f.readlines():
    xx = line.split()
    name = xx[0]
    date = xx[1]
    weekday = xx[2]
    duration = xx[3]


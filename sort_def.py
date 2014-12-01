# -*- coding: utf-8 -*-

__author__ = 'lpe234'
__date__ = '2014-11-30'


def sort_key(obj):
    sorted_list = [4, 2, 5, 9, 7, 8, 1, 3, 6, 0]
    return sorted_list.index(obj)


if __name__ == '__main__':
    print sorted(range(10), key=sort_key)
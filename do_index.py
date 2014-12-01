# -*- coding: utf-8 -*-

__author__ = 'lpe234'
__date__ = '2014-11-30'


class InvertedIndex(object):

    index_dict = {}

    def __init__(self):
        """
        1、建立索引
        :return:
        """
        line_index = 1
        while 1:
            words_line = raw_input(u"不含标点，若干单词由空格分隔 > ")
            if words_line:
                for word in words_line.split():
                    if word in self.index_dict:
                        self.index_dict[word].add(str(line_index))
                    else:
                        self.index_dict[word] = set(str(line_index), )
                line_index += 1
            else:
                break

    def print_index(self):
        """
        2、输出索引
        :return:
        """
        for key, values in sorted(self.index_dict.items(), key=lambda x: x[0]):
            print "{0} : {1}".format(key, ' ,'.join(str(x) for x in sorted(list(values))))

    def query_index(self):
        """
        3、检索
        :return:
        """
        while 1:
            keys_input = raw_input(u'输入查询字符串 > ')
            if keys_input.startswith('OR:'):
                keys_input = keys_input.replace('OR:', '')
                line_index = sorted(list(reduce(lambda x, y: x | y, [self.index_dict[key] for key in keys_input.split()])))
                index_result = ' ,'.join(str(x) for x in sorted(line_index))
                if not index_result:
                    index_result = None
                query_result = "{0} : {1}".format(keys_input, index_result)
            else:
                keys_input = keys_input.replace('AND:', '')
                line_index = sorted(list(reduce(lambda x, y: x & y, [self.index_dict[key] for key in keys_input.split()])))
                index_result = ' ,'.join(str(x) for x in sorted(line_index))
                if not index_result:
                    index_result = None
                query_result = "{0} : {1}".format(keys_input, index_result)
            print query_result


if __name__ == '__main__':
    invert = InvertedIndex()
    invert.print_index()
    invert.query_index()
#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestFilter(object):

    """
    filter: 过滤函数，根据fun返回Ture保留参数
    """
    def is_odd(self, num):
        return num%2 == 1

    def test_filter(self):
        list_num = [13, 34, 25, 26, 69, 10]
        result_list = filter(self.is_odd, list_num)
        print "[13, 25, 69]", result_list

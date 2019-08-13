#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestIteration(object):

    def test_iteration_list(self):
        lists = [1, 2, 2, 4, 5]
        for num in lists:
            print num
        for index, value in enumerate(lists):
            print index, ":", value

    def test_iteration_string(self):
        string = "ABC"
        for str in string:
            print str

    def test_iteration_tuple(self):
        tuple_num = (1, 3, 4, 7, "5454")
        for num in tuple_num:
            print num

    def test_iteration_dict(self):
        dict_students = {'Tom': '66', 'Mark': '79'}
        # 默认循环的是key
        for key in dict_students:
            print key
        # 循环value
        for value in dict_students.itervalues():
            print value

        for key,value in dict_students.iteritems():
            print key, ":", value

    def test_iteration_special(self):
        special_list = [(1, 2), ("6", "6"), ("tr", "tr")]
        for x, y in special_list:
            print x, y

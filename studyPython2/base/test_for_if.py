#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestForIf(object):

    def test_if(self):
        x = ''
        if x:
            print 'x为非零数值、非空字符串、非空list'
        else:
            print 'x为零数值、空字符串或空list'

    def test_for(self):

        students = ['Tom', 'Json', 'Jim', 'Tony']

        for student in students:
            print student

        # result：5, 6,7,8,9
        for i in range(5, 10):
            print i

    def test_while(self):
        sum = 13
        while sum > 10:
            sum = sum -1
            print sum

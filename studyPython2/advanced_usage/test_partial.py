#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import functools


class TestPartial(object):

    """
     functools.partial 的作用就是，
     把一个函数的某些参数给固定住(也就是设置默认值)，返回一个新的函数
    """

    def add(self, x, y):
        return x+y

    def test_int(self):
        add2 = functools.partial(self.add, y=6)
        print add2(5)

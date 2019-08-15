#!/usr/bin/python
# vim: set fileencoding=utf-8 :
"""
高阶函数:一个函数就可以接收另一个函数作
为参数
"""


class TestHigherOrderFunc(object):

    def add(self, x, y, f):
        """

        :param x:
        :type :int
        :param y:
        :type :int
        :param f:
        :type :method

        :return:
        :rtype :int
        """
        return f(x) + f(y)

    def test_func_and_variable(self):

        # 函数本身也可以赋值给变量，即:变量可以指向函数
        variable = abs
        num = variable(-10)
        print num

    def test_higher_func(self):

        result = self.add(-5, 6, abs)
        print result

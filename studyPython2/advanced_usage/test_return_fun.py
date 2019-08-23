#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestReturnFun(object):

    """
    方法返回函数时，返回的函数只有调用的时候才会被执行
    每次返回的函数都是新的函数，即使传入参数相同
    """
    def return_fun(self, *args):
        def sum():
            origin = 0
            for num in args:
                origin = origin + num
            return origin
        return sum

    def test_return_fun(self):
        fun1 = self.return_fun(1, 2, 3, 4)
        fun2 = self.return_fun(1, 2, 3, 4)

        print fun1 == fun2
        result = fun1()
        print result

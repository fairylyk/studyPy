#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestArgsKwargs(object):

    def arg_method(self, *args):
        """
        函数接收可变长度的非关键字参数列表作为函数的输入
        """
        print
        for arg in args:
            print arg

    def kwargs_method(self, **kwargs):
        """
        函数接收可变长度的关键字参数列表作为函数的输入
        """
        print
        for key, value in kwargs.iteritems():
            print key + ":" + value

    def normal_arg(self, arg1, arg2, arg3):
        print
        print arg1, arg2, arg3

    def test_args(self):
        self.arg_method('Java', 'Python', 'C++')

    def test_kwargs(self):
        self.kwargs_method(Java='5', Python='6', C="3")

    def test_args_call_method(self):
        args = ('Java', 'Python', 'C++')
        kwargs = {'arg1': 'Java', 'arg2': 'Python', 'arg3': 'C++'}

        self.normal_arg('Java', 'Python', 'C++')
        print '----------------------------'
        self.normal_arg(*args)
        print '----------------------------'
        self.normal_arg(**kwargs)


#!/usr/bin/python
# vim: set fileencoding=utf-8 :

"""
如果一个函数定义中包含 yield 表达式，那么该函数是一个生成器函数（而非普通函数）。
实际上，yield 仅能用于定义生成器函数。
与普通函数不同，生成器函数被调用后，其函数体内的代码并不会立即执行，
而是返回一个生成器（generator-iterator）。
当返回的生成器调用成员方法时，相应的生成器函数中的代码才会执行
"""


class TestYield(object):

    def fib(self, max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            # 最后a等于b，b等于a+b
            a, b = b, a + b
            # print "--a:{a}-b:{b}--".format(a=a, b=b)
            n = n + 1

    def test_yield(self):

        # 获取生成器：列表生成式[]改为（）
        gen = (x * x for x in range(10))

        for num in self.fib(5):
            print num

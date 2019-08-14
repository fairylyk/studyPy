#!/usr/bin/python
# vim: set fileencoding=utf-8 :

"""
生成器 是在 for 循环的过程中不断计算出下一个元素，
并在适当的条件结束 for 循环
"""


class TestGenerator(object):

    def gen_by_yield(self, max):
        n, a, b = 0, 0, 1
        while n < max:
            yield b
            # 最后a等于b，b等于a+b
            a, b = b, a + b
            # print "--a:{a}-b:{b}--".format(a=a, b=b)
            n = n + 1

    def test_yield(self):

        # 获取生成器：(1)列表生成式[]改为（）
        #           (2)使用yield
        gen = (x * x for x in range(10))
        num_list = [x * x for x in range(10)]

        # 0
        print '---first', gen.next()

        # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        print '---list', num_list

        # 循环获取下面内容: 1, 4, 9, 16, 25, 36, 49, 64, 81
        for num in gen:
            print '-----gen', num

        for gen in self.gen_by_yield(5):
            print '-----yield', gen

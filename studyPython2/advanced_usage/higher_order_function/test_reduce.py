#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestReduce(object):

    def add(self, x, y):
        return x+y

    def map(self, x):
        return

    def reduce_num(self, x, y):
        return x*10+y

    def test_reduce_num(self):
        list_num = [1, 2, 3, 4]
        result_add = reduce(self.reduce_num, list_num)
        # 结果为1234， 即 （(1*10+2）*10+3)*10+4
        print result_add

    def test_reduce_add(self):
        list_num = [1, 2, 3, 4]
        result_add = reduce(self.add, list_num)
        # 结果为10， 即1+2+3+4
        print result_add

    def str2int(self, str):

        def fn(x, y):
            return x * 10 + y

        def char2num(str):
            return ({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[str])

        # return reduce(lambda x, y: x * 10 + y, map(char2num, str))
        # 和下面代码效果相同，具体参考lambda用法
        return reduce(fn, map(char2num, str))

    def test_str2int(self):
        str_list = ['1', '2', '3', '4', '5', '6']
        result = self.str2int(str_list)
        print result
#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestBaseFunction(object):

    def test_base_function(self):

        print
        print '11的绝对值为：', abs(-11)
        div = divmod(6, 3)
        print '6/3的商为：', div[0], '余数为: ', div[1]
        pass

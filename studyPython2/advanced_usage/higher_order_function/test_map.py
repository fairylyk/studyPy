#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestMap(object):

    """
    Map :将list的对象按照fun执行以后，返回结果
    """

    def func_param(self, num):
        return num*num

    def func_params(self, x, y):
        return x+y

    def test_map(self):
        list_num = [1, 2, 3, 4, 5, 6]
        map_result = map(self.func_param, list_num)

        # [1, 4, 9, 16, 25, 36]
        print map_result

        # 将数字转换为字符串
        # ['1', '2', '3', '4', '5', '6']
        map_str = map(str, list_num)
        print map_str

    def test_map_params(self):
        list_num = [1, 2, 3, 4, 5, 6]
        map_params = map(self.func_params, list_num, list_num)
        print map_params

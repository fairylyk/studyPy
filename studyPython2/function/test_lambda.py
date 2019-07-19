#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestLambda(object):

    """
    lambda:格式--> lambda arg1,arg2: expression

    """
    def test_lambda(self):
        # 没有参数, 当没有参数的时候调用时也应该添加（）
        lambda_none = lambda: 1 != 2
        print "\n没有参数lambda_none:", lambda_none
        print "没有参数lambda_none():", lambda_none()
        print bool(lambda: 1 != 2)
        # 一个参数
        lambda_one = lambda arg1: arg1+1 == 2
        print "一个参数", lambda_one(2)

        # 两个参数
        lambda_two = lambda arg1, arg2: arg1 > arg2
        print "两个参数", lambda_two(5, 8)

        # special usage
        # [(-1, -3), (1, 2), (3, 4)]
        num_list = [(1, 2), (3, 4), (-1, -3)]
        num_list.sort(key=lambda x: x[0])
        print num_list



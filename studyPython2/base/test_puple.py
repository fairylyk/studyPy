#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestTuple(object):
    classmates = ('Bob', 'Jim', 'Tom')
    pass

    # 当定义的的tuple只有一个参数时，因为括号还可以表示数学公式，为了避免歧义参数后面加逗号
    # tuple中的参数值不能改变，其他的和list一致
    # 执行结果： (1,) ------- 1
    def test_tuple(self):
        t = (1,)
        t1 = (1)
        print t, '-------', t1

        # 虽然tuple的指向不可变，但是对因为list属于可变的,所有仍然可变
        c1 = (1, 2, ['A', 'B'])

        print "(1, 2, ['A', 'B']) :", c1

        c1[2][0] = 'X'
        c1[2][1] = 'Y'
        print "(1, 2, ['X', 'Y'])", c1

#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestSlice(object):

    def test_slice(self):

        """
        list，tuple，string all can use slice
        """
        lists = [1, 2, 3, 3, 5]
        print "获取list的前三位[1, 2, 3]", lists[:3]
        print "获取list的第二位到第三位之间的内容[2, 3]", lists[1:3]

        # 0~99
        numbers = range(100)
        print "前十位[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]", numbers[:10]
        print "后十位[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]", numbers[-10:]
        print "前十位每隔两位取一个[0, 2, 4, 6, 8]", numbers[:10:2]

        print (
            "每隔五个取一个[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50,"
            " 55, 60, 65, 70, 75, 80, 85, 90, 95]", numbers[::5])

#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestSorted(object):

    """
    sorted : 排序默认为升序，可以自己编写排序方式，数字和字符串都可以
    """
    def reversed_cmp(self, x, y):
        if x > y:
            return -1
        if x < y:
            return 1
        return 0

    def test_scorted(self):
        list_num = [12, 43, 43, 54, 57, 73, 22]
        result_num =sorted(list_num)
        result_num_desc = sorted(list_num, self.reversed_cmp)
        print result_num
        print result_num_desc

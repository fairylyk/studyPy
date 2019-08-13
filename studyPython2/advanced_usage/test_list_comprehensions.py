#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestListComprehension(object):

    """
    快速生成list
    """
    def test_comprehension_range(self):
        range_list = range(1, 10)
        print range_list

    def test_comprehension_list(self):
        num_list = [1, 5, 6, 3]
        num_list2 = [1, 5, 6, 3]
        result_list = [num for num in num_list]

        # [1, 5, 6, 3]
        print result_list

        sum_list = [num + m for num in num_list
                    for m in num_list2 if m + num > 10]
        # [11, 11, 12]
        print sum_list

        greater_than_three = [num for num in num_list if num > 3]

        # [5, 6]
        print greater_than_three

    def test_comprehension_dict(self):
        d = {'x': 'A', 'y': 'B', 'z': 'C'}
        result_list = [k + '=' + v for k, v in d.iteritems()]
        print  result_list




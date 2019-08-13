#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestRecursiveFunc(object):

    def fact(self, num):
        if num == 1:
            print 1,
            return 1
        print "{num}*".format(num=num),
        return num * self.fact(num - 1)

    def test_recursive_func(self):
        print
        num = self.fact(3)
        print "=", num

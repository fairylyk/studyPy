#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestFunction(object):

    change_num = 5

    def print_change_detail(self, func, change_detail):
        for i in range(3):
            print '------'
            func()
        print "change_Detail====", change_detail

    def change_num(self, num):
        print "change_num():num", num
        print "change_num():change_num", num
        return self.change_num+num

    def test_internal_function(self):

        def get_detail():
            num = 3
            self.change_num = self.change_num+num
            print "get_detail--num", num,\
                "get_detail--changge_num", self.change_num

        self.print_change_detail(
            get_detail, self.change_num(3))

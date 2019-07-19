#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestAdvancedFunciton(object):

    def wait_for_condition(self, method):

        print '6666'
        print "wait_for_condition---------", str

    def return_result(self):

        arg1 = 'python'
        arg2 = 'java'
        arg3 = 'c'

        return arg1, arg2, arg3

    def test_function(self):
        print '555'
        if True:
            def wait_for_pdfgen_warning_message():
                return "wait_for_pdfgen_warning_message被调用了----------"

            self.wait_for_condition(wait_for_pdfgen_warning_message)

    def test_return_result(self):
        """
        方法可以返回多个结果，实际上返回的是tuple类型，也可以直接用多个对象去接收
        """
        get_result = self.return_result()
        a, b, c = self.return_result()
        print get_result
        print a, b, c

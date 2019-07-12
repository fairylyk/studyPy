#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestAdvancedFunciton(object):
    def wait_for_condition(self, method):
        print '6666'
        print "wait_for_condition---------", str

    def test_function(self):
        print '555'
        if True:
            def wait_for_pdfgen_warning_message():
                return "wait_for_pdfgen_warning_message被调用了----------"

            self.wait_for_condition(wait_for_pdfgen_warning_message)
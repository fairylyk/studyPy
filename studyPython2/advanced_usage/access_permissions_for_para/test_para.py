#!/usr/bin/python
# vim: set fileencoding=utf-8 :

from student import Student


class TestPara(object):

    def test_para(self):

        print Student._name
        print Student._Student__score

        student = Student()
        student.set_name("test")
        print student._name

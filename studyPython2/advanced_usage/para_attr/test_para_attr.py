#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import primary_student
from types import MethodType


def demo_set_age(self, age):
    self.age = age
    print '>>>>age={}'.format(self.age)


class TestParaAttr(object):

    def set_age(self, age):
        self.age = age

    def test_para_attr(self):
        int_num = 5
        # 获取类型
        print type(int_num)
        student = primary_student.TestPrimaryStudent()

        # 判断类型
        print isinstance(int_num, int)
        print isinstance(student, primary_student.TestPrimaryStudent)

        # 获取属性，及所有对象
        aa = student.__getattribute__("_name")
        print aa, dir(student)

    def test_add_method_for_instance(self):
        student = primary_student.TestPrimaryStudent()

        # 给student绑定方法
        student.set_age = MethodType(
            demo_set_age, student, primary_student.TestPrimaryStudent())
        student.set_age('111')
        print student.age

        # 给primary_student.TestPrimaryStudent绑定方法
        primary_student.TestPrimaryStudent.set_age = MethodType(
            demo_set_age, None, primary_student)

        primary_student_t = primary_student.TestPrimaryStudent()
        primary_student_t.set_age('111')
        print primary_student_t.age

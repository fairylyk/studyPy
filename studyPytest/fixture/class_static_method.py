#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import pytest


class TestClassStaticMethod(object):

    def base_method(self):
        """
        第一个参数必须为self
        :return:
        """
        self.base_name = 'base_method'
        print ""

    @classmethod
    def class_method(cls):
        """
        有装饰器以后，第一个参数必须为cls
        :return:
        """
        cls.clase_name = 'class_method'
        print ""

    @staticmethod
    def static_method(self):
        self.static_name = 'static_method'
        print ""

    def test_method(self):
        print

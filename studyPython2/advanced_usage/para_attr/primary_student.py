#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import pytest
import os


class TestPrimaryStudent(object):

    # 虽然我可以被访问，但是，请把我视为私有变量，不要随意访问
    _name = 'private name'
    # 不能直接访问 但是可以通过 _Student__score
    __score = "can't be access by out"

    __special__ = "special para"

    # 用tuple定义允许绑定的属性名称
    # 说明该对象只能有这些指定属性
    # 其他的不能被指定
    # 仅对当前类有效，继承的父类无效
    __slots__ = ('name', 'age', 'score', '_score')

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        return self._name

    @property
    def score(self):

        # @property，给score赋予了get属性
        return self.__score

    @score.setter
    def score(self, value):

        # @score.setter，给score赋予了set属性
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    def test_para_attr(self):
        self.score = 100
        int_num = 5
        print type(int_num)

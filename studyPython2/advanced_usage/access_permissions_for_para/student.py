#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class Student(object):

    # 虽然我可以被访问，但是，请把我视为私有变量，不要随意访问
    _name = 'private name'
    # 不能直接访问 但是可以通过 _Student__score
    __score = "can't be access by out"

    __special__ = "special para"

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        return self._name

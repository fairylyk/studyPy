#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import pytest


class TestScopeFun(object):
    """
    function : 每次case执行时都会被调用
    autouse : 为True时，case执行时自动调用
              为False时，调用激活fun，例如test_scope_base
    """
    @pytest.fixture(scope="function")
    def scope_fun_base(self):

        self.base_name = 'scope_fun_base'
        print 'function----------scope_fun_base'

    @pytest.fixture(scope="function", autouse=True)
    def scope_fun_autouse(self):

        self.scope_autouse = 'scope_fun_autouse'
        print 'function----------scope_fun_autouse'

    def test_scope_one(self):
        print "---content---one"

    def test_scope_two(self):
        print "---content---two"

    def test_scope_base(self, scope_fun_base):
        print "---content---base"
        print self.base_name


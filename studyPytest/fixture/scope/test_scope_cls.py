#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import pytest


class TestScopeCls(object):

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def scope_cls_base(cls):

        cls.scope_cls = 'scope_cls_base'
        print "scope_cls_base"

    def test_scope_one(self):
        print "---content---one", self.scope_cls

    def test_scope_two(self):
        print "---content---two", self.scope_cls
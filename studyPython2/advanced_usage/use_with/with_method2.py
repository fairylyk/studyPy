#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class WithMethod2(object):

    def __enter__(self):
        print
        print '__enter__2'

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        :param exc_type: error type
        :param exc_val:  error info
        :param exc_tb:   error position
        :return:
        """
        print '__exit__2'


def get_with_method2():
    return WithMethod2()

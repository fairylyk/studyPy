#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestArgsKwargs(object):

    #
    def test_args(self):
        print self


    def test_args_(self):

        import os
        has_found = False
        size = int(168335)
        with open(
                '/Users/yali/Documents/test/study/studyPy/studyPython2'
                '/advanced_usage/test_args_kwargs.py', 'r') as file:
            file.seek(168335)
            while True:
                line = file.readline()
                if not line:
                    break
                if 'ERROR' in line and 'Failed to retrieve customize logo error' in line:
                    has_found = True
                    break
        print has_found



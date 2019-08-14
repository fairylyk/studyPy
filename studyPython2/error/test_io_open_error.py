#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestIoOpenError(object):

    def test_args_(self):

        has_found = False
        size = int(168335)
        # when use import os  os.open():TypeError: an integer is required
        # os.open(file,flags[,mode])以某种或多种方式打开某文件，返回新打开文件的描述符
        # open() 返回文件对象
        import os
        os.open("")
        with open(
                '/Users/yali/Documents/test/study/studyPy/studyPython2'
                '/advanced_usage/test_args_kwargs.py', 'r') as file:
            file.seek(168335)
            while True:
                line = file.readline()
                if not line:
                    break
                if ('ERROR' in line and
                        'Failed to retrieve customize logo error' in line):
                    has_found = True
                    break
        print has_found

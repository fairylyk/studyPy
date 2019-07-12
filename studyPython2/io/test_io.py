#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import os
import codecs



class TestIo(object):

    def test_open_read(self):
        # 获取当前目录os.getcwd(), 拼接文件路径   test_io.py
        path = os.path.join(os.getcwd(), 'test_io.py')
        File = open(path, "w")
        pdfgen_log_contents=""
        File.write(pdfgen_log_contents)

        # 为了避免文件读写中出现错误导致文件无法关闭，添加try finally块
        try:
            # 'r' 文件可读，打开文件
            f = open(path, "r")
            # 读取文件信息，用str接收
            str = f.read()
            print str
        finally:
            # 关闭文件，使用完文件关闭，防止占用系统资源
            if f:
                f.close()

        # python 为了避免繁琐，引入with，可以自动调用close()方法
        with open("test_io.py", 'r') as f:
            print f.read(), ''

        with open("test_io.py", 'r') as f:
            # read一次性读取文件内容，
            # readlines读取每行
            # read（size）指定每次可读字节数
            for line in f.readlines():
                print (line.split()), '------'

    def test_unicde(self):

        path = os.path.join(os.getcwd(), 'data/image.png')
        f = open(path, 'r')
        # f.read().decode('gbk')
        print

    def test_get_contents(self):
        has_found = False
        path = os.path.join(os.getcwd(), 'data/pdfgen.log')
        with open(path, 'r') as f:
            file_context = f.read()
            lines = file_context.split(self.TEST_DATA_DIR["linux"])
            for line in reversed(lines):
                if 'ERROR' in line and 'Failed to retrieve customize logo error' in line:
                    has_found = True
                    break
        return has_found


    TEST_DATA_DIR = {
        'windows': '\r\n',
        'linux': '\n'
    }
    def get_remote_test_data_dir(self, os_type):
        """
        :type os_type: string
        :param os_type: windows or linux

        :rtype: string
        :return: the test_data_dir
        """
        return self.TEST_DATA_DIR[os_type.lower()]



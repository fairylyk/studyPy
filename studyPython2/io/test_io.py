#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import os
import codecs



class TestIo(object):

    def test_open_read(self):
        # 获取当前目录os.getcwd(), 拼接文件路径
        path = os.path.join(os.getcwd(), 'test_io.py')

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
        print char

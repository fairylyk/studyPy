#!/usr/bin/python
# vim: set fileencoding=utf-8 :

'''
第一行代码是为了告诉linux、os x系统。Python可执行。Windows会忽略
第二行代码告诉为为utf-8b编码格式，否则中文输出会报错
'''


class TestString(object):
    '''
    self is similar to this in java
    '''

    print '转换为ASCII编码', ord("A")

    print '转换为正常字符', chr(65)

    print len('a')

    # 常见占位符：
    # %d 整数
    # %f 浮点数
    # %s 字符串
    # %x 十六进制整数

    name = 'fairy'
    age = 18
    print ('dsdsd')
    print '%s 的年龄是 %d' % (name, age)

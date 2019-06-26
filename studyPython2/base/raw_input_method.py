#!/usr/bin/python
# vim: set fileencoding=utf-8 :

'''
the top should be added 'vim: set fileencoding=utf-8 :'
just for printing Chinese

第一行代码是为了告诉linux、os x系统。Python可执行。Windows会忽略
第二行代码告诉为为utf-8b编码格式，否则中文输出会报错
'''

name = raw_input()
old = raw_input('请输入你的年龄')
print  name, '的年龄是', old

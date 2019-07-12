#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import with_method


# with 语句适用于对资源进行访问的场合，
# 确保不管使用过程中是否发生异常都会执行必要的“清理”操作，
# 释放资源，比如文件使用后自动关闭／线程中锁的自动获取和释放等


class TestWith(object):
    """
    （１）紧跟with后面的语句被求值后，返回对象的“–enter–()”方法被调用，
         这个方法的返回值将被赋值给as后面的变量；
    （２）当with后面的代码块全部被执行完之后，将调用前面返回对象的“–exit–()”方法。
     (3)执行结果：
             __enter__
             running。。。。。。
             __exit__
    """

    def test_with(self):
        # with with_method.get_with_method():
        #     print 'running。。。。。。'

        with with_method.get_with_method() as f1, \
                with_method.get_with_method() as f2:
            print 'running2。。。。。。'

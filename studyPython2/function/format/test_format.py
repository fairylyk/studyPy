#!/usr/bin/python
# vim: set fileencoding=utf-8 :
import example_object


class TestFormat(object):

    def test_param(self):

        # 不指定位置，默认位置： test format
        print "{} {}".format("test", "format")

        # 指定位置：format test
        print "{1} {0}".format("test", "format")

        # 参数名字：打印信息：加油 ,时间：2019
        print "打印信息：{detail} ,时间：{time}".format(detail="加油", time="2019")

        # 列表索引设置参数"0" 是必须的：打印信息：菜鸟 ,时间：学习
        my_list = ['菜鸟', '学习']
        print "打印信息：{0[0]} ,时间：{0[1]}".format(my_list)

        # 传入对象
        example_value = example_object.ExampleObject(6)
        print ('value为:{0.value}'.format(example_value))  # value为:6
        print ('value为:{.value}'.format(example_value))   # 0可以省略：value为:6
        print ('key为:{0.key}'.format(example_value))     # key为:7

    def test_format_number(self):
        # :.2f结果：3.15
        # :+.2f结果:+3.15
        # :.0f结果:3
        # :0 > 2d结果:03
        # :x < 4d结果:3xxx
        # :, 结果:1, 000, 000
        # :.2 % 结果:314.54 %
        # :.2e结果：1.00e+09
        # : > 10d结果：         6
        # : < 10d结果：6

        print
        print ":.2f结果：{:.2f}".format(3.14535)
        print ":+.2f结果:{:+.2f}".format(3.14535)
        print ":.0f结果:{:.0f}".format(3.14535)
        print ":0>2d结果:{:0>2d}".format(3)
        print ":x<4d结果:{:x<4d}".format(3)
        print ":,结果:{:,}".format(1000000)
        print ":.2%结果:{:.2%}".format(3.14535)
        print ":.2e结果：{:.2e}".format(1000000000)
        print ":>10d结果：{:>10d}".format( 6 )
        print ":<10d结果：{:<10d}".format(   6 )





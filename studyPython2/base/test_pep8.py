#!/usr/bin/python
# vim: set fileencoding=utf-8 :
# 1、在class行与上面有内容的时候，应该间隔两行
# 2、class命名应该使用骆驼命名法：首字母大写



class TestPep8(object):
    pass

    # 方法名为小写
    # 方法与上面内容间隔为一行

    # 逗号后面应该有空格
    # 等号左右两边有空格
    #
    def test_show_parameter(self):
        # 垂直缩进：对准左括号的第一个字符
        self.test_show_parameter('发斯蒂芬是否发的是飞洒地方', '发送到发大水发多发发',
                                 '防守打法打发第三方的发的发发防守打法', '发对方答复')
        # 悬挂式缩进：以首字母为基准，缩进
        self.test_show_parameter(
            '发斯蒂芬是否发的是飞洒地方', '发送到发大水发多发发',
            '防守打法打发第三方的发的发发防守打法', '发对方答复')

        my_list = [
            'q', 're', 're',
            1, 4, 3, 5
        ]  # 右括号回退
        a = 'fd'
        pass

    def many_parameters(self, first, second, third, four):
        # 每行代码不超过79个字符
        # 没有括号续行
        with open('') as file_1, \
                open('', 'w') as file_2:
            pass
        print 'aa'

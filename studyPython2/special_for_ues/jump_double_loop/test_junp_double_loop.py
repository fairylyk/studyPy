#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestJumpDoubleLoop(object):

    def test_jump_return(self):
        print
        for num in range(5):
            for change_num in range(5):
                print "外层循环，内层循环：", num, change_num
                if change_num > 2:
                    return
                else:
                    print "外层循环，内层循环：", num, change_num

    def test_jump_for_else(self):
        # ~~~~~~
        # 外层循环，内层循环： 0 0
        # 外层循环，内层循环： 0 1
        # 外层循环，内层循环： 0 2
        # 外层循环，内层循环： 0 3
        # 外层循环，内层循环： 0 4
        # if ： 0 4
        # 66666666

        print
        for num in range(5):
            print '~~~~~~'
            for change_num in range(5):
                print "外层循环，内层循环：", num, change_num
                change = num+change_num
                if change > 3:
                    print "if：", num, change_num
                    # 跳出第二层循环
                    break
            else:
                print '~0000000'
                # 当第二次循环break，跳出第一层循环，继续第一层循环
                continue
            print '66666666'
            break



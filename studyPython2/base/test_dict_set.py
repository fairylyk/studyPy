#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestDictSet(object):
    """
    dict相比较list
    dict：
     1、查找，插入快
     2、浪费内存
     3、key顺序与添加顺序没有关系
    """
    def test_dict(self):
        dict_students = {'Tom': '66', 'Mark': '79'}
        print dict_students['Tom']

        # 假如key不存在，将会报错：dict_students['Lily']
        # 避免key不存在情况
        # 1、 in
        # 2、get:如果不存在返回None，或者指定返回值 eg：-1
        if 'Mark' in dict_students:
            print dict_students['Mark']

        print dict_students.get('Lily')
        print dict_students.get('School')
        print dict_students.get('Lily', -1), dict_students

        dict_students['Tom'] = 8             # 更新
        dict_students['School'] = "RUNOOB"   # 添加
        del dict_students['Tom']             # 删除key
        dict_students.clear()                # 清空
        del dict_students                    # 删除dict_students

    def test_set(self):
        s1 = set([1, 2, 7, 7])
        s2 = set([1, 5, 6])
        print ''
        print s1       # result:set([1, 2, 7])
        s1.add('e')    # 添加
        s1.remove(2)   # 删除
        print s1       # set([1, 'e', 7])
        print s1 & s2  # 交集set([1])
        print s1 | s2  # 并集set([1, 'e', 5, 6, 7])
        print s1 - s2  # 差集set(['e', 7])
        print s2 - s1  # 差集set([5, 6])
        s3 = set({"Tom": "A", "Far": "B"})
        print set(s3)      # set(['Far', 'Tom'])
        for i in s3:
            print i, '-------'

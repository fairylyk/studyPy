#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestList(object):
    classmates = ['Tony', 12, True]
    print 'classmates\'s length :', len(classmates)

    print 'get the first element :', classmates[0]

    print 'get the last element :', classmates[-1]

    classmates.append("Nina")

    classmates.insert(0, 'Lily')
    print 'add a element :', classmates
    # delete the last one
    classmates.pop()
    print 'print classmates :', classmates
    # delete the specified one
    classmates.pop(1)
    print 'delete the specified one:', classmates

    classmates[1] = 'Change'
    print 'change the specified one:', classmates
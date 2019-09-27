#!/usr/bin/python
# vim: set fileencoding=utf-8 :
from mammal import Mammal
from runnable import Runnable


class Dog(Mammal, Runnable):

    def leg(self):
        print "I have leg"

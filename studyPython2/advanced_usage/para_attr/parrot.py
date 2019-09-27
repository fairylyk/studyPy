#!/usr/bin/python
# vim: set fileencoding=utf-8 :
from bird import Bird
from flyable import Flyable


class Parrot(Bird, Flyable):

    def wing(self):
        print "I have wing"
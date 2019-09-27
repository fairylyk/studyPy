#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class CustomClasses(object):

    def __init__(self, name):
        self.name = name
        self.num1, self.num2 = 1, 2

    def __str__(self):
        return self.name

    def __iter__(self):
        return self

    def base_usage(self):
        print 'rrr'

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
               a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                    a, b = b, a+b
            return L

    def next(self):
        self.num1, self.num2 = self.num2, self.num2+self.num1
        print self.num1, self.num2
        if self.num1 > 10:  # 退出循环
            raise StopIteration()
        return self.num1


print
print "--------", CustomClasses("ddd")[:5]

print "dd"
for n in CustomClasses("111"):
    print n
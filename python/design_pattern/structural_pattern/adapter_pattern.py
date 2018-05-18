# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals


# base implementation of adapter pattern
# 适配模式是结构设计模式， 实现两个不兼容接口的兼容，保持程序的开放/封闭原则， 保持新老代码间的兼容


class OldClass(object):
    def talk(self):
        return "this is old class talk methods"

    def __str__(self):
        return "old class"


class newClass(object):
    def executor(self):
        return "this is new class executor methods"

    def __str__(self):
        return "new class"


class Adapter(object):
    def __init__(self, obj, adapter_methods):
        self.__obj = obj
        self.__dict__.update(adapter_methods)

    def __str__(self):
        return str(self.__obj)


def main():
    objects = [newClass()]
    old_class_obj = OldClass()
    objects.append(Adapter(old_class_obj, dict(executor=old_class_obj.talk)))

    for o in objects:
        print("{}, {}".format(str(o), o.executor()))


if __name__ == "__main__":
    main()

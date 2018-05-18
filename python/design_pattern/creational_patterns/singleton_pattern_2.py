# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function


class Singleton(type):
    def __new__(cls, name, bases, attrs):
        print("__new__")
        attrs["_instance"] = None
        return super(Singleton, cls).__new__(cls, name, bases, attrs)

    def __call__(self, *args, **kwargs):
        print("__call__")
        if self._instance is None:
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
        return self._instance


class Foo(object):
    __metaclass__ = Singleton


if __name__ == "__main__":
    foo1 = Foo()
    foo2 = Foo()

    print(id(foo1) == id(foo2))

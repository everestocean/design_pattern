# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function


# 在讲到使用元类创建单例模式之前，比需了解__new__这个内置方法的作用，在上面讲元类的时候我们用到了__new__方法来实现类的创建。然而我在那之前还是对__new__这个方法和__init__方法有一定的疑惑。因此这里花点时间对其概念做一次了解和区分。
#
# __new__方法负责创建一个实例对象，在对象被创建的时候调用该方法它是一个类方法。__new__方法在返回一个实例之后，会自动的调用__init__方法，对实例进行初始化。如果__new__方法不返回值，或者返回的不是实例，那么它就不会自动的去调用__init__方法。
#
# __init__ 方法负责将该实例对象进行初始化，在对象被创建之后调用该方法，在__new__方法创建出一个实例后对实例属性进行初始化。__init__方法可以没有返回值。
#
# __call__方法其实和类的创建过程和实例化没有多大关系了，定义了__call__方法才能被使用函数的方式执行。


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    assert id(s1) == id(s2), "s1 is not equal s2"

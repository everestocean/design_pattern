# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import ABCMeta, abstractmethod


# base implement of bridge pattern
# Bridge pattern: Decouple an abstraction from its implementation so that the two can vary independently.
# 桥接模式（Bridge Pattern）用于将”抽象”(abstraction, 比如接口或算法)与实现方式相分离。
# 如果不用桥接模式，那么通常的写法是，创建若干个基类，用于表示各种抽象方式，然后从每个基类中继承出两个或多个子类，
# 用于表示对这种抽象方式的不同实现办法。用了桥接模式之后，我们需要创建两套独立的”类体系”：“抽象体系”定义了我们要执行的操作
# （比如接口或高层算法），而”实现体系”则包含具体实现方式，抽象体系要调用实体体系以完成其操作。
# 抽象体系中的类会把实现体系中的某个类实例聚合起来，而这个实例将充当抽象接口与具体实现之间的桥梁（bridge）。


class AbstractDrawImplementor(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_square(self, side):
        pass


class DrawImplementorA(AbstractDrawImplementor):
    def draw_square(self, side):
        print("This is draw implement A with side {}".format(side))


class DrawImplementorB(AbstractDrawImplementor):
    def draw_square(self, side):
        print("This is draw implement B with side {}".format(side))


class Square(object):
    def __init__(self, side, draw_implementor_obj):
        self.side = side
        if not isinstance(draw_implementor_obj, AbstractDrawImplementor):
            raise ValueError("Invalid input, input draw implementor {} is not valid implementor object!".format(
                draw_implementor_obj))
        self.draw_implementor_obj = draw_implementor_obj

    def draw(self):
        self.draw_implementor_obj.draw_square(self.side)

    def resize(self, new_side):
        self.side = new_side


if __name__ == "__main__":
    square_a = Square(1, DrawImplementorA())
    square_a.draw()

    square_b = Square(2, DrawImplementorB())
    square_b.draw()

    try:
        square_c = Square(1, None)
    except ValueError as e:
        print(e.message)

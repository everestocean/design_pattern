# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

# base implement of facade pattern
# 为子系统中的一组接口提供一个统一的入口。外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。
# 外观模式优点：
# 减少客户端所需处理的对象数目，使得子系统使用起来更加容易。
# 实现了子系统与客户端之间的松耦合关系。
# 一个子系统的修改对其他子系统没有任何影响，而且子系统内部变化也不会影响到外观对象。
# 外观模式缺点：
# 不能很好地限制客户端直接使用子系统类，如果对客户端访问子系统类做太多的限制则减少了可变性和灵活性。
# 如果设计不当，增加新的子系统可能需要修改外观类的源代码，违背了开闭原则。


class SubSystemOne(object):

    def method_one(self):
        print("SubSystem One!")


class SubSystemTwo(object):

    def method_two(self):
        print("SubSystem two!")


class SubSystemThree(object):

    def method_three(self):
        print("SubSystem three!")


class Facade(object):

    def __init__(self):
        self.p_one_obj = SubSystemOne()
        self.p_two_obj = SubSystemTwo()
        self.p_three_obj = SubSystemThree()

    def method_a(self):
        print("Facade::MethodA")
        self.p_one_obj.method_one()
        self.p_two_obj.method_two()

    def method_b(self):
        print("Facade::MethodB")
        self.p_two_obj.method_two()
        self.p_three_obj.method_three()


if __name__ == "__main__":
    facade_obj = Facade()
    facade_obj.method_a()
    facade_obj.method_b()

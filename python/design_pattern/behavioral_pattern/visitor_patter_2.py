# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import abstractmethod, ABCMeta


# base implementation of visitor pattern
# 提供一个作用于某对象结构中的各元素的操作表示，它使我们可以在不改变各元素的类的前提下定义作用于这些元素的新操作。访问者模式是一种对象行为型模式。
# 一个对象结构包含多个类型的对象，希望对这些对象实施一些依赖其具体类型的操作。在访问者中针对每一种具体的类型都提供了一个访问操作，不同类型的对象可以有不同的访问操作。
# 需要对一个对象结构中的对象进行很多不同的并且不相关的操作，而需要避免让这些操作“污染”这些对象的类，也不希望在增加新操作时修改这些类。
# 访问者模式使得我们可以将相关的访问操作集中起来定义在访问者类中，对象结构可以被多个不同的访问者类所使用，将对象本身与对象的访问操作分离。


class ElementNode(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def accept(self, visitor_obj):
        pass


class ConcreteElementNodeA(ElementNode):
    def accept(self, visitor_obj):
        visitor_obj.visit(self)

    def operation_a(self):
        print("ConcreteElementNodeA")


class ConcreteElementNodeB(ElementNode):
    def accept(self, visitor_obj):
        visitor_obj.visit(self)

    def operation_b(self):
        print("ConcreteElementNodeB")


class Vistor(object):
    def visit(self, element_obj):
        if isinstance(element_obj, ConcreteElementNodeA):
            self.visit_element_a(element_obj)
        elif isinstance(element_obj, ConcreteElementNodeB):
            self.visit_element_b(element_obj)

    def visit_element_a(self, element_obj):
        element_obj.operation_a()

    def visit_element_b(self, element_obj):
        element_obj.operation_b()


class ObjectStructure(object):
    def __init__(self):
        self.node_list = list()

    def action(self, visitor_obj):
        for node in self.node_list:
            node.accept(visitor_obj)

    def add(self, element_node):
        self.node_list.append(element_node)


if __name__ == "__main__":
    object_structure_obj = ObjectStructure()
    object_structure_obj.add(ConcreteElementNodeA())
    object_structure_obj.add(ConcreteElementNodeB())

    visitor_obj = Vistor()
    object_structure_obj.action(visitor_obj)

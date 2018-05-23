# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import abstractmethod, ABCMeta


# base implementation of template pattern
# Define the skeleton of an algorithm in an operation, deferring some steps to subclasses.
# Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.


class AbastractTemplate(object):
    __metaclass__ = ABCMeta

    def template_method(self):
        self.primiary_operation_one()
        self.primiary_operation_two()
        self.concrete_operation()
        self.hook()

    @abstractmethod
    def primiary_operation_one(self):
        pass

    @abstractmethod
    def primiary_operation_two(self):
        pass

    def concrete_operation(self):
        print("Mandatory Operations for all ConcreteClasses")

    def hook(self):
        pass


class ConcreteTemplateA(AbastractTemplate):
    def primiary_operation_one(self):
        print("primitiveOp1 A")

    def primiary_operation_two(self):
        print("primitiveOp2 A")


class ConcreteTemplateB(AbastractTemplate):
    def primiary_operation_one(self):
        print("primitiveOp1 B")

    def primiary_operation_two(self):
        print("primitiveOp2 B")

    def hook(self):
        print("hook B")


if __name__ == "__main__":
    concreate_a_obj = ConcreteTemplateA()
    concreate_b_obj = ConcreteTemplateB()


    concreate_a_obj.template_method()
    concreate_b_obj.template_method()

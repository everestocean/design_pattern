# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import abstractmethod, ABCMeta


# base implementation of interpret pattern
# 定义一个语言的文法，并且建立一个解释器来解释该语言中的句子，这里的“语言”是指使用规定格式和语法的代码。解释器模式是一种类行为型模式。
# 解释器模式优点：
#   易于改变和扩展文法。
#   每一条文法规则都可以表示为一个类，因此可以方便地实现一个简单的语言。
#   实现文法较为容易。在抽象语法树中每一个表达式节点类的实现方式都是相似的，这些类的代码编写都不会特别复杂，还可以通过一些工具自动生成节点类代码。
#   增加新的解释表达式较为方便。如果用户需要增加新的解释表达式只需要对应增加一个新的终结符表达式或非终结符表达式类，原有表达式类代码无须修改，符合“开闭原则”。
# 解释器模式缺点：
#   对于复杂文法难以维护。在解释器模式中，每一条规则至少需要定义一个类，因此如果一个语言包含太多文法规则，类的个数将会急剧增加，
#   导致系统难以管理和维护，此时可以考虑使用语法分析程序等方式来取代解释器模式。
#   执行效率较低。由于在解释器模式中使用了大量的循环和递归调用，因此在解释较为复杂的句子时其速度很慢，而且代码的调试过程也比较麻烦。


class Expression(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def interpret(self, context_obj):
        pass


class Constant(Expression):
    def __init__(self, i):
        self.i = i

    def interpret(self, context_obj):
        return self.i


class Variable(Expression):
    def interpret(self, context_obj):
        return context_obj.lookup_value(self)


class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context_obj):
        return self.left.interpret(context_obj) + self.right.interpret(context_obj)


class Sub(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context_obj):
        return self.left.interpret(context_obj) - self.right.interpret(context_obj)


class Mul(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context_obj):
        return self.left.interpret(context_obj) * self.right.interpret(context_obj)


class Div(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context_obj):
        return self.left.interpret(context_obj) / self.right.interpret(context_obj)


class Context(object):
    def __init__(self):
        self.map = dict()

    def add_value(self, variable_obj_x, y):
        self.map[variable_obj_x] = y

    def lookup_value(self, variable_obj_x):
        return self.map.get(variable_obj_x)


if __name__ == "__main__":
    context_obj = Context()

    a = Variable()
    b = Variable()
    c = Constant(15000)

    context_obj.add_value(a, 14)
    context_obj.add_value(b, 10000)

    expression_obj = Div(Mul(a, b), Add(Sub(a, b), c))
    print("Result = {}".format(expression_obj.interpret(context_obj)))

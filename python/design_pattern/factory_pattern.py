# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import ABCMeta, abstractmethod
import math


AreaCalculatorFactries = dict()
DEFAULT_SQUARE_AREA_CALCULATOR = "square"
DEFAULT_CIRCLE_AREA_CALCULATOR = "circle"


class AbstractAreaCalculator(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculator(self, length, *args, **kwargs):
        pass


class AreaCalculatorFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self, parameters=None, *args, **kwargs):
        pass


class SquareAreaCalculator(AbstractAreaCalculator):
    def calculator(self, length, *args, **kwargs):

        return length**2


class SquareAreaCalculatorFactory(AreaCalculatorFactory):
    def create(self, parameters=None, *args, **kwargs):
        return SquareAreaCalculator()


class CircleAreaCalculator(AbstractAreaCalculator):
    def calculator(self, length, *args, **kwargs):

        return math.pi*((length/2)**2)


class CircleAreaCalculatorFactory(AreaCalculatorFactory):
    def create(self, parameters=None, *args, **kwargs):
        return CircleAreaCalculator()


def register(calculator_name, calculator_factories_obj=None):
    if calculator_factories_obj is None or not isinstance(calculator_factories_obj, AreaCalculatorFactory):
        print("Register calculator factory failed, because input calculator factory object is invalid!")
    else:
        registered = AreaCalculatorFactries.get(calculator_name, None)
        if registered:
            print("Register calculator factory failed, because the factory of {} is already exist!".format(calculator_name))
        AreaCalculatorFactries[calculator_name] = calculator_factories_obj


register(DEFAULT_SQUARE_AREA_CALCULATOR, SquareAreaCalculatorFactory())
register(DEFAULT_CIRCLE_AREA_CALCULATOR, CircleAreaCalculatorFactory())


def create(calculator_name, parameters=None):
    area_calculator_factory_obj = AreaCalculatorFactries.get(calculator_name, None)
    if area_calculator_factory_obj is None:
        print("create area calculator factory object failed, because the factory is not found!")
    else:
        return area_calculator_factory_obj.create(parameters)


if __name__ == "__main__":
    length = 10
    print("{}".format("#"*10))
    print("Calculate Square Area with length {}".format(length))
    square_area_calculator_obj = create(DEFAULT_SQUARE_AREA_CALCULATOR)
    area = square_area_calculator_obj.calculator(length)
    print("The Square Area is {}".format(area))

    print("{}".format("#"*10))
    print("Calculate Circle Area with diameter {}".format(length))
    circle_area_calculator_obj = create(DEFAULT_CIRCLE_AREA_CALCULATOR)
    area = circle_area_calculator_obj.calculator(length)
    print("The Circle Area is {}".format(area))

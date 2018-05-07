# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import ABCMeta, abstractmethod


# base implementation of factory pattern


class BaseFigureAbstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def desc(self):
        pass


class Circle(BaseFigureAbstract):
    def desc(self):
        print("This is circle!")


class Rectangle(BaseFigureAbstract):
    def desc(self):
        print("This is rectangle!")


class Triangle(BaseFigureAbstract):
    def desc(self):
        print("This is triangle!")


class SimpleFigrueFactory(object):
    TYPE_CIRCLE = 1
    TYPE_RECTANGLE = 2
    TYPE_TRIANGLE = 3

    def create_figure(self, figure_type):

        if figure_type == self.TYPE_CIRCLE:
            return Circle()
        elif figure_type == self.TYPE_RECTANGLE:
            return Rectangle()
        elif figure_type == self.TYPE_TRIANGLE:
            return Triangle()
        else:
            print("Unknown figure type!")


if __name__ == "__main__":
    simple_figure_factory_obj = SimpleFigrueFactory()

    circle_obj = simple_figure_factory_obj.create_figure(figure_type=1)
    circle_obj.desc()

    triangle_obj = simple_figure_factory_obj.create_figure(figure_type=3)
    triangle_obj.desc()

    rectangle_obj = simple_figure_factory_obj.create_figure(figure_type=2)
    rectangle_obj.desc()

# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import abstractmethod, ABCMeta


# base implement of decorator pattern
# 装饰者的特点
# 装饰者和被装饰对象有相同的超类型。
# 你可以用一个或多个装饰者包装一个对象。
# 既然装饰者和被装饰对象有相同的超类型，所以在任何需要原始对象（被包装的）的场合，可以用装饰过的对象代替它。
# 装饰者可以在所委托被装饰者的行为之前与/或之后，加上自己的行为，以达到特定的目的。
# 对象可以在任何时候被装饰，所以可以在运行时动态地、不限量地用你喜欢的装饰者来装饰对象。

class AbstractWindow(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


class SimpleWindow(AbstractWindow):
    def draw(self):
        print("draw windows")

    def get_description(self):
        return "Simple Windows"


class WindowDecorator(AbstractWindow):
    def __init__(self, decorated_window_obj):
        self.decorated_window_obj = decorated_window_obj


class VerticalScrollBarDecorator(WindowDecorator):
    def draw(self):
        self.vertical_scroll_bar_decorator_draw()
        self.decorated_window_obj.draw()

    def vertical_scroll_bar_decorator_draw(self):
        print("draw vertical scroll bar window")

    def get_description(self):
        return self.decorated_window_obj.get_description() + " with vertical scroll bar"


class HorizontalScrollBarDecorator(WindowDecorator):
    def draw(self):
        self.horizontal_scroll_bar_decorator_draw()
        self.decorated_window_obj.draw()

    def horizontal_scroll_bar_decorator_draw(self):
        print("draw horizontal scroll bar window")

    def get_description(self):
        return self.decorated_window_obj.get_description() + " with horizontal scroll bar"


if __name__ == "__main__":
    simple_window_obj = SimpleWindow()
    print(simple_window_obj.get_description())

    vertical_scroll_bar_window_obj = VerticalScrollBarDecorator(simple_window_obj)
    print(vertical_scroll_bar_window_obj.get_description())

    horizontal_scroll_bar_window_obj = HorizontalScrollBarDecorator(simple_window_obj)
    print(horizontal_scroll_bar_window_obj.get_description())

    vertical_horizontal_scroll_bar_window_obj = VerticalScrollBarDecorator(simple_window_obj)
    vertical_horizontal_scroll_bar_window_obj = HorizontalScrollBarDecorator(vertical_horizontal_scroll_bar_window_obj)
    print(vertical_horizontal_scroll_bar_window_obj.get_description())

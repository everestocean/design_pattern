# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import ABCMeta, abstractmethod


# base implementation of state pattern
# 允许对象在内部状态改变时改变它的行为, 对象看起来好像修改了它的类.
# 当控制一个对象的状态转换的条件表达式过于复杂时,把状态的判断逻辑转移到表示不同状态的一系列类当中,可以把复杂的判断逻辑简化
# (当一个对象的行为取决于它的状态,并且它必须在运行时刻根据状态改变他的行为)


class State(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def write_program(self, w):
        pass


class Work(object):
    def __init__(self):
        self.hour = 9
        self.curr = ForenoonState()

    def set_state(self, s):
        self.curr = s

    def write_program(self):
        self.curr.write_program(self)


class ForenoonState(State):
    def write_program(self, w):
        if w.hour < 12:
            print("Current time {}, is time for forenoon!".format(w.hour))
        else:
            w.set_state(AfternoonState())
            w.write_program()


class AfternoonState(State):
    def write_program(self, w):
        if w.hour < 17:
            print("Current time {}, is time for afternoon".format(w.hour))
        else:
            w.set_state(EveningState())
            w.write_program()


class EveningState(State):
    def write_program(self, w):
        if w.hour < 21:
            print("Current time {}, is time for evening".format(w.hour))
        else:
            w.set_state(SleepState())
            w.write_program()


class SleepState(State):
    def write_program(self, w):
        print("Current time {}, is time for sleeping".format(w.hour))


if __name__ == "__main__":
    work_obj = Work()
    work_obj.hour = 9
    work_obj.write_program()
    work_obj.hour = 15
    work_obj.write_program()
    work_obj.hour = 20
    work_obj.write_program()
    work_obj.hour = 22
    work_obj.write_program()

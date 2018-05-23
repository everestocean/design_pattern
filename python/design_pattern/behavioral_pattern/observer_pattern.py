# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import datetime


# base implementation of observer pattern
# 定义了对象之间的一对多依赖，这样一来，当一个对象改变状态时，
# 它的所有依赖都会收到通知并自动更新。观察者模式提供了一种对象设计，让主题和观察者之间松耦合。


class Observer(object):
    def update(self, subject_obj):
        pass


class Subject(object):
    def __init__(self):
        self.observer_list = list()

    def attach_(self, observer_obj):
        self.observer_list.append(observer_obj)

    def detach_(self, observer_obj):
        if observer_obj in self.observer_list:
            self.observer_list.remove(observer_obj)

    def notify(self):
        for observer in self.observer_list:
            observer.update(self)


class ClickTimer(Subject):
    def __init__(self):
        self.time_tuple = datetime.datetime.now().timetuple()
        super(ClickTimer, self).__init__()

    def get_hour(self):
        return int(self.time_tuple.tm_hour)

    def get_minute(self):
        return int(self.time_tuple.tm_min)

    def get_second(self):
        return int(self.time_tuple.tm_sec)

    def tick(self):
        self.time_tuple = datetime.datetime.now().timetuple()
        self.notify()


class DigitalClock(Observer):
    def __init__(self, click_time_obj):
        self.subject = click_time_obj
        self.subject.attach_(self)

    def update(self, subject_obj):
        if self.subject == subject_obj:
            self.draw()

    def draw(self):
        hour = self.subject.get_hour()
        minute = self.subject.get_minute()
        second = self.subject.get_second()

        print("Digital time is {}:{}:{}".format(hour, minute, second))


class AnalogClock(Observer):
    def __init__(self, click_time_obj):
        self.subject = click_time_obj
        self.subject.attach_(self)

    def update(self, subject_obj):
        if self.subject == subject_obj:
            self.draw()

    def draw(self):
        hour = self.subject.get_hour()
        minute = self.subject.get_minute()
        second = self.subject.get_second()

        print("Analog time is {}:{}:{}".format(hour, minute, second))


if __name__ == "__main__":
    timer = ClickTimer()

    digist_clock_obj = DigitalClock(timer)
    analog_clock_obj = AnalogClock(timer)

    timer.tick()

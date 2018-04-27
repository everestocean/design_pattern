# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals


# base implementation of Chain of Responsibility Pattern


class DefaultHandler(object):
    def __init__(self, successor=None):
        self.__successor = successor

    def handler(self, event):
        if self.__successor is not None:
            self.__successor.handler(event)


class ConcreteHandler1(DefaultHandler):
    def handler(self, event):
        if event >= 0 and event < 5:
            print("In handler1 {}".format(event))
        else:
            super(ConcreteHandler1, self).handler(event)


class ConcreteHandler2(DefaultHandler):
    def handler(self, event):
        if event >= 5 and event < 10:
            print("In handler2 {}".format(event))
        else:
            super(ConcreteHandler2, self).handler(event)


class ConcreteHandler3(DefaultHandler):
    def handler(self, event):
        if event >= 10 and event < 15:
            print("In handler3 {}".format(event))
        else:
            super(ConcreteHandler3, self).handler(event)


class ConcreteHandler4(DefaultHandler):
    def handler(self, event):
        if event >= 15 and event < 20:
            print("In handler4 {}".format(event))
        else:
            super(ConcreteHandler4, self).handler(event)


class Client(object):
    def __init__(self):
        self.handler = ConcreteHandler4(ConcreteHandler3(ConcreteHandler2(ConcreteHandler1(DefaultHandler()))))

    def delegate(self, requests):
        for request in requests:
            self.handler.handler(request)


if __name__ == "__main__":
    client_obj = Client()
    requests = [2, 3, 10, 19, 8, 9, 1, 0]

    client_obj.delegate(requests)

# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import abstractmethod, ABCMeta


# base implement of proxy pattern
# Proxy provides an interface that forwards function calls to another interface of the same form.
# A Proxy pattern is useful to modify the behavior of the RealSubject class while still preserving
# its interface. This is particularly useful if the RealSubject class is in third-party library
# and hence not easily modifiable directly. There are other use cases of Proxy:
# 1. Implement lazy instantiation of the RealSubject object
#     In this case, the RealSubject object is not actually instantiated until a method call is invoked.
#     This can be useful if instantiating the RealSubject object is a heavyweight operation that we wish
#     to defer until absolutely necessary.
# 2. Implement access control to the RealSubject object
#     We may want to insert a permissions layer between the Proxy and the RealSubject objects to ensure
#     that users can only call certain methods on the RealSubject object if they have appropriate permission.
# 3. Support debug or dry-run modes
# 4. Make the RealSubject class to be thread safe
# 5. Share resources
# 6. Protect against future changes in the RealSubject class


class AbstractSubject(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def request(self):
        pass


class RealSubject(AbstractSubject):
    def request(self):
        print("RealSubject request!")


class Proxy(AbstractSubject):
    def __init__(self, real_subject_obj=None):
        if real_subject_obj is not None:
            self.real_subject_obj = real_subject_obj
        else:
            self.real_subject_obj = RealSubject()

    def request(self):
        self.real_subject_obj.request()


if __name__ == "__main__":
    proxy_obj = Proxy()
    proxy_obj.request()

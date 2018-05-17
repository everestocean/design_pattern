# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import ABCMeta, abstractmethod


# base implement of flyweight
# 享元模式，以共享的方式高效地支持大量的细粒度的对象。通过复用内存中已存在的对象，降低系统创建对象实例的性能消耗。
# 当系统中某个对象类型的实例较多的时候。
# 由于使用了大量的对象，造成了很大的存储开销。
# 对象的大多数状态都可变为外蕴状态。
# 在系统设计中，对象实例进行分类后，发现真正有区别的分类很少的时候。

class AbstractWebSite(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def use(self):
        pass


class ConcreteWebSite(AbstractWebSite):
    def __init__(self, name):
        self.name = name

    def use(self, user):
        print("Web category: {} user {}".format(self.name, user))


class WebSiteFlyWeightFactory(object):
    def __init__(self):
        self.web_sites = dict()

    def get_web_site_category(self, key):
        if not self.web_sites.has_key(key):
            self.web_sites[key] = ConcreteWebSite(key)
        return self.web_sites[key]

    def get_web_site_count(self):
        print(len(self.web_sites))


if __name__ == "__main__":
    web_site_flyweight_factory_obj = WebSiteFlyWeightFactory()

    fx = web_site_flyweight_factory_obj.get_web_site_category("product_display")
    fy = web_site_flyweight_factory_obj.get_web_site_category("product_display")
    fz = web_site_flyweight_factory_obj.get_web_site_category("product_display")
    fx.use("user_a")
    fy.use("user_b")
    fz.use("user_c")

    web_site_flyweight_factory_obj.get_web_site_count()

    fx = web_site_flyweight_factory_obj.get_web_site_category("blog")
    fy = web_site_flyweight_factory_obj.get_web_site_category("blog")
    fz = web_site_flyweight_factory_obj.get_web_site_category("blog")
    fx.use("user_d")
    fy.use("user_e")
    fz.use("user_f")
    web_site_flyweight_factory_obj.get_web_site_count()

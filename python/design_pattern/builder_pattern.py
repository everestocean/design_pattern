# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import ABCMeta, abstractmethod


# base implementation of builder pattern
# 构建模式，将一个复杂对象的构建与它的表示分离,使得同样的构建过程可以创建不同的表示


class VehicleBuilder(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def make_wheels(self):
        pass

    @abstractmethod
    def make_doors(self):
        pass

    @abstractmethod
    def make_seats(self):
        pass


class CarBuilder(VehicleBuilder):
    def make_wheels(self):
        print("This is car, have 4 wheels")

    def make_doors(self):
        print("This is car, have 3 doors")

    def make_seats(self):
        print("This is car, have 5 seats")


class BikeBuilder(VehicleBuilder):
    def make_wheels(self):
        print("This is bike, have 2 wheels")

    def make_doors(self):
        print("This is bike, have 0 doors")

    def make_seats(self):
        print("This is bike, have 2 seats")


class VehicleManufacturer(object):
    def __init__(self, builder):
        self.builder = builder

    def create(self):
        assert isinstance(self.builder, VehicleBuilder), "No define builder"
        self.builder.make_wheels()
        self.builder.make_doors()
        self.builder.make_seats()


if __name__ == "__main__":
    car_builder_obj = CarBuilder()
    bike_builder_obj = BikeBuilder()

    car_manufacturer_obj = VehicleManufacturer(car_builder_obj)
    car_manufacturer_obj.create()

    bike_manufacturer_obj = VehicleManufacturer(bike_builder_obj)
    bike_manufacturer_obj.create()

# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import abstractmethod, ABCMeta


# base implement composite pattern
# 组合模式: 允许你将对象组合成树形结构来表现"整体/部分"层次结构. 组合能让客户以一致的方法处理个别对象以及组合对象.
# 建立组件类(Component), 组合类(composite)和叶子类(leaf)继承组件类, 客户类(client)直接调用最顶层的组合类(composite)即可.


class NotImplementException(Exception):
    pass


class AbstractMenuComponent(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, menu_component_obj):
        pass

    @abstractmethod
    def remove(self, menu_component_obj):
        pass

    @abstractmethod
    def get_child(self, index):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def is_vegetarian(self):
        pass

    @abstractmethod
    def printf(self):
        pass


class MenuItem(AbstractMenuComponent):
    def __init__(self, name, description=None, vegetarian=False, price=0.0):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def is_vegetarian(self):
        return self.vegetarian

    def printf(self):
        if self.is_vegetarian():
            print(" {}(v), {}".format(self.get_name(), self.get_price()))
        else:
            print(" {}, {}".format(self.get_name(), self.get_price()))
        print("  --{}".format(self.get_description()))

    def add(self, menu_component_obj):
        raise NotImplementException("Not implement!")

    def remove(self, menu_component_obj):
        raise NotImplementException("Not implement!")

    def get_child(self, index):
        raise NotImplementException("Not implement!")


class Menu(AbstractMenuComponent):
    def __init__(self, name, description=None):
        self.name = name
        self.description = description

        self.menu_items_list = list()

    def add(self, menu_component_obj):
        self.menu_items_list.append(menu_component_obj)

    def remove(self, menu_component_obj):
        self.menu_items_list.remove(menu_component_obj)

    def get_child(self, index):
        if index > len(self.menu_items_list):
            raise ValueError("Index out range")
        else:
            return self.menu_items_list[index]

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def printf(self):
        print("\n {}, {}".format(self.get_name(), self.get_description()))
        print("{}".format("-" * 20))

        for item in self.menu_items_list:
            item.printf()

    def get_price(self):
        raise NotImplementException("Not implement!")

    def is_vegetarian(self):
        raise NotImplementException("Not implement!")


class Waitress(object):
    def __init__(self, all_menus_obj):
        self.all_menus_obj = all_menus_obj

    def print_menus(self):
        self.all_menus_obj.printf()


if __name__ == "__main__":
    pancakeHouse_menu = Menu("PANCAKE HOUSE MENU", "Breakfast")
    diner_menu = Menu("DINER MENU", "Lunch")
    cafe_menu = Menu("CAFE MENU", "Dinner")
    dessert_menu = Menu("DESSERT MENU", "Dessert course!")

    all_menus = Menu("ALL MENUS", "All menus combined")

    all_menus.add(pancakeHouse_menu)
    all_menus.add(diner_menu)
    all_menus.add(cafe_menu)
    all_menus.add(dessert_menu)

    pancakeHouse_menu.add(MenuItem(
        "Regular Pancake Breakfast",
        "Pancakes with fried eggs, sausage",
        False,
        2.99))

    diner_menu.add(MenuItem(
        "Vegetarian BLT",
        "(Fakin') Bacon with lettuce & tomato on whole wheat",
        True,
        2.99))
    diner_menu.add(MenuItem(
        "BLT",
        "Bacon with lettuce & tomato on whole wheat",
        False,
        2.99))

    dessert_menu.add(MenuItem(
        "Cheesecake",
        "Creamy New York cheesecake, with a chocolate graham crust",
        True,
        1.99))
    dessert_menu.add(MenuItem(
        "Sorbet",
        "A scoop of raspberry and a scoop of lime",
        True,
        1.89))

    cafe_menu.add(MenuItem(
        "Veggie Burger and Air Fries",
        "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
        True,
        3.99))
    cafe_menu.add(MenuItem(
        "Soup of the day",
        "A cup of the soup of the day, with a side salad",
        True,
        3.69))

    waitress = Waitress(all_menus)
    waitress.print_menus()

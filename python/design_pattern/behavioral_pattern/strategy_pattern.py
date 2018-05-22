# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import abstractmethod, ABCMeta


# base implementation of strategy pattern
# 定义了算法族, 分别封装起来, 让它们之间可以相互替换, 此模式让算法的变化独立于使用算法的客户.
#

class SortBehavior(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def sort_operation(self):
        pass


class Merge(SortBehavior):
    def sort_operation(self):
        print("Merge sorted")


class Quick(SortBehavior):
    def sort_operation(self):
        print("Quick sorted")


class Heap(SortBehavior):
    def sort_operation(self):
        print("Heap sorted")


class SearchBehavior(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def search(self):
        pass


class Sequential(SearchBehavior):
    def search(self):
        print("Seuqential search")


class BinaryTree(SearchBehavior):
    def search(self):
        print("Binary Tree search")


class HashTable(SearchBehavior):
    def search(self):
        print("Hash table search")


class Collection(object):
    def __init__(self):
        self.sort_behavior_obj = None
        self.search_behavior_obj = None

    def set_sort_behavior(self, sort_behavior_obj):
        self.sort_behavior_obj = sort_behavior_obj

    def set_search_behavior(self, search_behavior_obj):
        self.search_behavior_obj = search_behavior_obj

    def sort_operation(self):
        self.sort_behavior_obj.sort_operation()

    def search(self):
        self.search_behavior_obj.search()


if __name__ == "__main__":
    merge_sort_obj = Merge()
    quick_sort_obj = Quick()
    heap_sort_obj = Heap()

    sequential_search_obj = Sequential()
    binary_tree_search_obj = BinaryTree()
    hash_table_search_obj = HashTable()

    collection_obj_one = Collection()
    collection_obj_one.set_sort_behavior(merge_sort_obj)
    collection_obj_one.sort_operation()

    collection_obj_two = Collection()
    collection_obj_two.set_search_behavior(sequential_search_obj)
    collection_obj_two.search()

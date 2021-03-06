# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import datetime


# base implementation of memento pattern
# Memento模式保存了封装的边界，一个Memento对象是另一种原发器对象的表示，
# 不会被其他代码改动。这种模式简化了原发器对象，Memento只保存原发器的状态。采用堆栈备忘对象，可以实现多次取消操作。
# 下面的情景很适合应用备忘录模式：
#   1.对象状态的备忘足以使对象可以完全恢复到原来的状态。
#   2.使用一个直接的接口来取得状态会使实现细节过程化，这样会打破对象的封装性。


class GameRole(object):
    def __init__(self, blood_volume=None, attack=None, defense=None):
        self.blood_volume = blood_volume if blood_volume is not None else 100
        self.attack = attack if attack is not None else 100
        self.defense = defense if defense is not None else 100

    def save_game_role(self):
        print("{} save game role!".format(datetime.datetime.now().strftime('%b-%d-%y %H:%M:%S')))
        return RoleStateMemento(self.blood_volume, self.attack, self.defense)

    def resume_game_role(self, role_state_memento_obj):
        print("{} resume game role".format(datetime.datetime.now().strftime('%b-%d-%y %H:%M:%S')))

        self.blood_volume = role_state_memento_obj.get_blood_volume()
        self.attack = role_state_memento_obj.get_attack()
        self.defense = role_state_memento_obj.get_defense()

    def show_game_role(self):
        print("role base information")
        print("Blood {}".format(self.blood_volume))
        print("Attack {}".format(self.attack))
        print("Defense {}".format(self.defense))

    def get_blood_volume(self):
        return self.blood_volume

    def set_blood_volume(self, blood_volume):
        self.blood_volume = blood_volume

    def get_attack(self):
        return self.attack

    def set_attack(self, attack):
        self.attack = attack

    def get_defense(self):
        return self.defense

    def set_defense(self, defense):
        self.defense = defense


class RoleStateMemento(object):
    def __init__(self, blood_volume, attack, defense):
        self.blood_volume = blood_volume
        self.attack = attack
        self.defense = defense

    def get_blood_volume(self):
        return self.blood_volume

    def set_blood_volume(self, blood_volume):
        self.blood_volume = blood_volume

    def get_attack(self):
        return self.attack

    def set_attack(self, attack):
        self.attack = attack

    def get_defense(self):
        return self.defense

    def set_defense(self, defense):
        self.defense = defense


class RoleStateCarataker(object):
    def __init__(self):
        self.role_state_mementor_obj = None

    def get_role_state_mementor(self):
        return self.role_state_mementor_obj

    def set_role_state_mementor(self, role_state_mementor_obj):
        self.role_state_mementor_obj = role_state_mementor_obj


if __name__ == "__main__":
    game_role_obj = GameRole()
    print("{} backup before{}".format("*" * 10, "*" * 10))
    game_role_obj.show_game_role()

    role_state_carataker_obj = RoleStateCarataker()
    role_state_carataker_obj.set_role_state_mementor(game_role_obj.save_game_role())

    game_role_obj.set_blood_volume(20);
    game_role_obj.set_attack(58)
    game_role_obj.set_defense(84)
    print("{} backup after {}".format("*" * 10, "*" * 10))

    game_role_obj.show_game_role()

    print("{} read the mementor {}".format("*" * 10, "*" * 10))
    game_role_obj.resume_game_role(role_state_carataker_obj.get_role_state_mementor())
    game_role_obj.show_game_role()

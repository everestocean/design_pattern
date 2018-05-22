# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import ABCMeta, abstractmethod

# base implementation of command pattern
# 命令模式 将“请求”封装成对象，以便使用不同的请求，队列或者日志来参数化其他对象。命令模式也支持可撤销的操作
# 适用场景：
#   系统需要将请求调用者和请求接收者解耦，使得调用者和接收者不直接交互。
#   统需要在不同的时间指定请求、将请求排队（如：线程池+工作队列）和执行请求。
#   系统需要支持命令的撤销(Undo)操作和恢复(Redo)操作
#   系统需要将一组操作组合在一起，即支持宏命令
# 优点：
#   降低系统的耦合度:Command模式将调用操作的对象与知道如何实现该操作的对象解耦。
#   Command是头等的对象。它们可像其他的对象一样被操纵和扩展。
#   组合命令:你可将多个命令装配成一个组合命令，即可以比较容易地设计一个命令队列和宏命令。一般说来，组合命令是Composite模式的一个实例。
#   增加新的Command很容易，因为这无需改变已有的类
#   可以方便地实现对请求的Undo和Redo。
# 缺点：
#   使用命令模式可能会导致某些系统有过多的具体命令类。因为针对每一个命令都需要设计一个具体命令类，因此某些系统可能需要大量具体命令类，这将影响命令模式的使用。
#

# command interface
class Command(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


# Reciver class
class Light(object):

    def On(self):
        print("The light is on")

    def Off(self):
        print("The light is off")


# command for turning on the light
class LightOnCommand(Command):

    def __init__(self, light_obj):
        self.light_obj = light_obj

    def execute(self):
        self.light_obj.On()


# command for turning off the light
class LightOffCommand(Command):

    def __init__(self, light_obj):
        self.light_obj = light_obj

    def execute(self):
        self.light_obj.Off()


# Ivoker
# Store the ConcreteCommand object
class RemoteControl(object):

    def __init__(self):
        self.command_obj = None

    def set_command(self, command_obj):
        self.command_obj = command_obj

    def button_press(self):
        self.command_obj.execute()


if __name__ == "__main__":
    light_obj = Light()

    light_on_command_obj = LightOnCommand(light_obj)
    light_off_command_obj = LightOffCommand(light_obj)

    control_obj = RemoteControl()

    control_obj.set_command(light_on_command_obj)
    control_obj.button_press()
    control_obj.set_command(light_off_command_obj)
    control_obj.button_press()

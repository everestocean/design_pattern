# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from abc import abstractmethod, ABCMeta


# base implementation of mediator pattern
# 中介者模式的优点就是减少类之间的依赖，把原有的一对多的依赖变成了一对一的依赖，同事类只依赖中介者，减少了类的依赖，当然也降低了类间的耦合。
# 适用场景：
# 一组定义良好的对象，现在要进行复杂的相互通信。
# 想通过一个中间类来封装多个类中的行为，而又不想生成太多的子类。
# 优点：
#  1. 简化了对象之间的关系，将系统的各个对象之间的相互关系进行封装，将各个同事类解耦，使得系统变为松耦合。
#  2. 提供系统的灵活性，使得各个同事对象独立而易于复用。
# 缺点：
#  1. 中介者模式中，中介者角色承担了较多的责任，所以一旦这个中介者对象出现了问题，整个系统将会受到重大的影响
#  2. 新增加一个同事类时，不得不去修改抽象中介者类和具体中介者类，此时可以使用观察者模式和状态模式来解决这个问题。


class AbstractMediator(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.concrete_colleague_one_obj = None
        self.concrete_colleague_two_obj = None

    def get_concrete_colleague_one(self):
        return self.concrete_colleague_one_obj

    def get_concrete_colleague_two(self):
        return self.concrete_colleague_two_obj

    def set_concrete_colleague_one(self, colleague_one_obj):
        self.concrete_colleague_one_obj = colleague_one_obj

    def set_concrete_colleague_two(self, colleague_two_obj):
        self.concrete_colleague_two_obj = colleague_two_obj

    @abstractmethod
    def do_something_one(self):
        pass

    @abstractmethod
    def do_something_two(self):
        pass


class ConcreteMediator(AbstractMediator):
    def do_something_one(self):
        print("ConcreteMediator----doSomethingOne()")
        self.concrete_colleague_one_obj.do_self_method()

    def do_something_two(self):
        print("ConcreteMediator----doSomethingTwo()")
        self.concrete_colleague_two_obj.do_self_method()


class AbstractColleague(object):
    __metaclass__ = ABCMeta

    def __init__(self, mediator_obj):
        self.mediator_obj = mediator_obj

    @abstractmethod
    def do_self_method(self):
        pass

    @abstractmethod
    def do_dep_method(self):
        pass


class ConcreteColleague1(AbstractColleague):
    def __init__(self, mediator_obj):
        super(ConcreteColleague1, self).__init__(mediator_obj)

    def do_self_method(self):
        print("ConcreteColleague1----doSelfMethod()")

    def do_dep_method(self):
        print("ConcreteColleague1----doDepMethod()")
        self.mediator_obj.do_something_one()


class ConcreteColleague2(AbstractColleague):
    def __init__(self, mediator_obj):
        super(ConcreteColleague2, self).__init__(mediator_obj)

    def do_self_method(self):
        print("ConcreteColleague2----doSelfMethod()")

    def do_dep_method(self):
        print("ConcreteColleague2----doDepMethod()")
        self.mediator_obj.do_something_two()


# fly example

class Fly(object):
    TYPE_IN = "in"
    TYPE_OUT = "out"
    ID = None
    name = None

    def __init__(self, ID=None, name=None):
        self.airport_mediator = None
        self.ID = ID
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.ID

    def set_id(self, ID):
        self.ID = ID

    def get_airport_mediator(self):
        return self.airport_mediator

    def set_airport_mediator(self, airport_mediator):
        self.airport_mediator = airport_mediator

    @abstractmethod
    def do_self_method(self, Type):
        # 定义飞机执行自己的操作
        pass

    @abstractmethod
    def do_dep_method(self, Type):
        # 定义飞机执行与机场调度中心的操作
        pass

    @abstractmethod
    def In(self):
        # 定义飞机进站操作
        pass

    @abstractmethod
    def Out(self):
        # 定义飞机出站操作
        pass

    @abstractmethod
    def listen_airport_mediator_notification(self, notification):
        # 定义飞机监听机场调度中心的通知
        pass


class ConcreteFly(Fly):
    def __init__(self, name, ID):
        super(ConcreteFly, self).__init__(ID, name)

    def do_self_method(self, type):
        print("ConcreteFly---doSelfMethod")
        print("Fly: " + self.name + "---" + type.lower())

    def do_dep_method(self, Type):
        print("ConcreteFly---doDepMethod")
        print("Fly: " + self.name + "---" + Type.lower())
        self.airport_mediator.do_manager(self, Type)

    def In(self):
        print("ConcreteFly---in()---Fly:" + self.name + "---------in")
        self.do_self_method(self.TYPE_IN)
        self.do_dep_method(self.TYPE_IN)

    def Out(self):
        print("ConcreteFly---out()---Fly:" + self.name + "--------out")
        self.do_self_method(self.TYPE_OUT)
        self.do_dep_method(self.TYPE_OUT)

    def listen_airport_mediator_notification(self, notification):
        print("ConcreteFly----listerMediatorNotification")
        print("Fly:" + self.name + "--lister Mediator Notification:" + notification)


class AirportMediator(object):
    def __init__(self):
        self.fly_list = list()

    def add(self, fly_obj):
        self.fly_list.append(fly_obj)

    def remove(self, fly_obj):
        self.fly_list.remove(fly_obj)

    def do_manager(self, fly_obj, Type):
        print("AirportMediator---doManager")
        if (Type.lower() == fly_obj.TYPE_IN):
            if fly_obj not in self.fly_list:
                self.add(fly_obj)
        elif (Type.lower() == fly_obj.TYPE_OUT):
            if fly_obj in self.fly_list:
                self.remove(fly_obj)

        for f in self.fly_list:
            f.listen_airport_mediator_notification(
                "Mediator Notification:Fly:" + fly_obj.get_name() + "---" + Type.lower() + "---各个飞机按命令调度")


if __name__ == "__main__":
    mediator_obj = ConcreteMediator()

    colleague_one_obj = ConcreteColleague1(mediator_obj)
    colleague_two_obj = ConcreteColleague2(mediator_obj)

    mediator_obj.set_concrete_colleague_one(colleague_one_obj)
    mediator_obj.set_concrete_colleague_two(colleague_two_obj)

    print("-" * 20)
    colleague_one_obj.do_self_method()
    print("-" * 20)
    colleague_one_obj.do_dep_method()
    print("-" * 20)
    colleague_two_obj.do_self_method()
    print("-" * 20)
    colleague_two_obj.do_dep_method()
    print("-" * 20)

    print("#" * 30)
    print("Airport Mediator example!")

    airport_mediator_obj = AirportMediator()

    fly_obj_one = ConcreteFly("001", 1)
    fly_obj_two = ConcreteFly("002", 2)
    fly_obj_three = ConcreteFly("003", 3)

    fly_obj_one.set_airport_mediator(airport_mediator_obj)
    fly_obj_two.set_airport_mediator(airport_mediator_obj)
    fly_obj_three.set_airport_mediator(airport_mediator_obj)

    print("-" * 20)
    fly_obj_one.In()
    print("-" * 20)
    fly_obj_two.In()
    print("-" * 20)
    fly_obj_three.In()
    print("-" * 20)
    fly_obj_one.Out()
    print("-" * 20)
    fly_obj_two.Out()
    print("-" * 20)
    fly_obj_three.Out()
    print("-" * 20)

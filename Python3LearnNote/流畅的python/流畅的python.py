"""
可选参数设置为默认值可以保证api在进化的同时能保证向后兼容


"""

# charles = {'name': 'Charles L. Dodgson', 'born': 1832}
#
# lewis = charles
#
# print(lewis is charles) # True
#
# print(id(lewis)) # 4308216880
# print(id(charles)) # 4308216880
#
# lewis['test'] = 900
# print(charles) # {'name': 'Charles L. Dodgson', 'born': 1832, 'test': 900}
#
# alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'test': 900}
#
# print(alex == charles) # True 指的是赋值内容是一样的
# print(alex is not charles) # True 比较两个对象，结果相等， 这是因为dict类的__eq__方法就是这样实现的


import copy


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    bus1 = Bus(['alice', 'bill', 'claire', 'david'])
    bus2 = copy.copy(bus1) # bus2和bus1共享一个列表，因为是浅复制
    bus3 = copy.deepcopy(bus1)
    print(id(bus1), id(bus2), id(bus3))
    print(bus1.passengers)
    bus1.drop('bill')
    print(bus1.passengers, bus2.passengers, bus3.passengers)
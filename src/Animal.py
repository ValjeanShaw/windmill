# 定义类
class Animal(object):
    # 类属性
    num = 0

    # 构造方法
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        # 私有属性
        self.__types = ""
        Animal.num += 1

    # 普通方法
    def shout(self):
        print(self.name + "的叫声：" + self.sound)

    # 私有方法
    def __fun(self):
        print("我是私有方法")

    # 类方法
    @classmethod
    def get_num(cls):
        return cls.num

    # 静态方法
    @staticmethod
    def hello():
        print("hello,i`m static method")

    # 静态方法
    @staticmethod
    def hello2(filed):
        print("hello,i`m static method filed is :", filed)

    # 私有属性配套的getter和setter方法
    def get_type(self):
        return self.__types

    def set_type(self, types):
        self.__types = types


# 继承
class Dog(Animal):
    def __init__(self, name, sound, num):
        super(Dog, self).__init__(name, sound)
        self.num = num

    # 重写   子类重写父类方法
    def shout(self):
        print(self.name + "变异重写后的叫声:" + self.sound)

    # 相同的方法，后面的方法会覆盖前面的方法
    def shout(self):
        print(self.name, "变异重写后的叫声:", self.sound, self.num, "次")


animal = Animal("猫", "喵")
# 隐藏属性
animal.sex = 'man'
print(animal.sex)
animal.shout()

dog = Dog("狗", "汪汪", 3)
dog.shout()

dog.set_type("animal")
print(dog.get_type())

Animal("动物", "叫").shout()

print(Animal.num)
print(Animal.get_num())
print(animal.get_num())
print(Animal.hello())
print(animal.hello())
print(Animal.hello2(1))
print(animal.hello2(2))

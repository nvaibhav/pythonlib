import os


class Apple:
    manufacturer = "Apple Inc."
    website = "www.apple.com"
    _whereami = "I am a protected variable"
    __whereami = "I am a private variable"
    def whereami(self):
        print("I am in Apple class")
        print(self.__whereami)

class OperatingSystem:
    os = "MacOS"
    def whereami(self):
        print("I am in OperatingSystem class, with os :",self.os)

class Macbook(Apple,OperatingSystem):
    def __init__(self):
        print("Macbook's manufacturer is {} and site {} ".format(self.manufacturer, self.website))
    def whereami1(self):
        print("I am in Macbook class")
        super().whereami()
    def whereami(self):
        print("where am i:",self._whereami)
        print("where am i:",super().whereami())


mymacbook = Macbook()
mymacbook.whereami()

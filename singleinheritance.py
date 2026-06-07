class Apple:
    manufacturer = "Apple Inc."
    website = "www.apple.com"
    def whereami(self):
        print("I am in Apple class")

class Macbook(Apple):
    def __init__(self):
        print("Macbook's manufacturer is {} and site {} ".format(self.manufacturer, self.website))
    def whereami1(self):
        print("I am in Macbook class")
        super().whereami()


mymacbook = Macbook()
mymacbook.whereami()

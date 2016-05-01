class Parent:
    parentAttr = 19

    def __init__(self):
        print("Construtor da classe mae")

    def parentMethod(self):
        print("this is the parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("parent attribute: ", Parent.parentAttr)

    def contador(self):
        print("this is a counter")


class Child(Parent):
    def __init__(self):
        print("calling child contructor")

    def childMethod(self):
        print("calling child method")

    def contador(self):
        print("contador filho")



c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.contador()
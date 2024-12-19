class animal:
    def speak(self):
        return "snimals can speak"

class dog(animal):
    def barks(self):
        return "it barks"
    
ra=dog()
print(ra.speak())
print(ra.barks())



# multiple inheritance
class transportation:
    def transport(self):
        return "transportation transport the onjects"

class car(transportation):
    def speed(self):
        return "It is no so fast"
class bike(transportation):
    def speed1(self):
        
        return "It is  so fast"
ba=bike()
ca=car()
print(ca.transport())
print(ca.speed())
print(ba.transport())
print(ba.speed1())



# multilevel in heritance

class A:
    def method1(self):
        return "1"
class B(A):
    def method2(self):
        return "2"

class C(B):
    def method1(self):
        return "3"

c=C()
print(c.method1())






# Super()

class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        return self.height*self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length , length)

sq=Square(2)
print(sq.area())




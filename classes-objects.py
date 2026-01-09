# Classes and Objects
# Object is an instance of class.
# Object Property - 1] Every object should be uniquely identified.
#                   2] Every object created has its own behaviour.

# Class is a code template on how to create an object.

class Person(): # Class
    def __init__(self, name, age, profession): # init is initializer or constructor, self will initialize itself.
        self.name = name
        self.age = age
        self.profession = profession

    def show(self):
        print(self.name)
        print(self.age)
        print(self.profession)

    def work(self):
        print(f"{self.name} is working as {self.profession}")

print(Person)

A = Person(name="Shubham", age=27, profession="Engineer") # Object
print(A)

A.show()
A.work()

B = Person("Virat", 36, "Cricketer")
B.show()
B.work()

# Create a Calculator using classes and objects.
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        A = self.num1 + self.num2
        return A
    def sub(self):
        B = self.num1 - self.num2
        return B
    def mul(self):
        C = self.num1 * self.num2
        return C
    def div(self):
        D = self.num1 / self.num2
        return D

x = Calculator(59, 76)
print(x)

print(x.add())
print(x.sub())
print(x.mul())
print(x.div())
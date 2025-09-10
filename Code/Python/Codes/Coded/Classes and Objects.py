class Person:
    def __init__ (self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def describe(self):
        print(f"I am {self.name} i like the color {self.color} i am {self.age} years old.")

my_Person = Person("John", "Blue", "18")
your_Person = Person("Roberto", "Brown", "35")

my_Person.describe()
your_Person.describe()
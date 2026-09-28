#!/usr/bin/env python3

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(isinstance(dog, Dog))
print(isinstance(Cat, Animal))

print(issubclass(Cat, Animal))

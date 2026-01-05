# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):  # overriding parent method
        return f"{self.name} barks."


# Another child class
class Cat(Animal):
    def speak(self):  # overriding parent method
        return f"{self.name} meows."


# Using the classes
dog = Dog("Tommy")
cat = Cat("Kitty")

print(dog.speak())  # Tommy barks.
print(cat.speak())  # Kitty meows.

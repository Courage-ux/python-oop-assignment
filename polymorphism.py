class Animal:
    def speak(self):
        pass  # Placeholder method

class Dog(Animal):
    def speak(self):
        print("Woof! 🐕")

class Cat(Animal):
    def speak(self):
        print("Meow! 🐈")

dog = Dog()
cat = Cat()

dog.speak()  # Woof! 🐕
cat.speak()  # Meow! 🐈
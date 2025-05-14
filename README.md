# python-oop-assignment

--book_class.py
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

    def add_pages(self, new_pages):
        self.pages += new_pages
        print(f"{new_pages} pages added! The book now has {self.pages} pages.")

book = Book("Python for Beginners", "John Doe", 200)
book.display_info()
book.add_pages(50)
book.display_info()



--polymorphism.py
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


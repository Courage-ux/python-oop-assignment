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
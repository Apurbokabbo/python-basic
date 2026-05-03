class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def display(self):
        return f'Title: {self.title}\nAuthor: {self.author}\nCopies: {self.copies}'

# Object Creation
# book1 = Book("SQA", "Test", 10)
title = input("Enter title: ")
author = input("Enter author: ")
copies = int(input("Enter copies: "))
book1 = Book(title, author, copies)
print(book1.display())
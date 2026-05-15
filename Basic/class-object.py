class Book:
    def __init__(self,name,author,copy):
        self.name=name
        self.author=author
        self.copy=copy

    def display(self):
        return f"Name :{self.name} Author:{self.author} Copies:{self.copy}"


#Object create
book1=Book("SQA","Apurbo Kabbo","333")
print(book1.display())

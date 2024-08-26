class BookShelf:
    def __init__(self, *books):
        self.books = books
        
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."
    
shelf = BookShelf(300)

# print(shelf)

class Book:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"Book {self.name}"
    
book = Book("LOTR")
book2 = Book("The Da Vinci Code")
shelf = BookShelf(book, book2)

print(book)
print(book2)
print(shelf)

print(shelf.books)

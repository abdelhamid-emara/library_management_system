# Used To Store All Books In Our Library When Program Runs
books_list = []

class Book:
    def __init__(self, title : str, author : str, copies : int):
        # Initializing Attributes
        self.title = title.strip().capitalize()
        self.author = author.strip().capitalize()
        self.copies = copies
    
    def __str__(self):
        return f"Book Title: {self.title} \nBook Author: {self.author} \nCopies: {self.copies}"
    
    def __repr__(self):
        return f"({self.title}, by {self.author})"
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author 
        return False
        
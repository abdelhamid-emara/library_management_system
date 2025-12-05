import baseclass, book, utils

# Used To Store All Members When Program Runs
members_list = []

# Member Class Inherits Person Class
class Member(baseclass.Person):
    def __new__(cls, *args, **kwargs):
        # Create Temporary Object Just To Compare
        obj = super().__new__(cls)
        if len(args) >= 2: 
            obj.name, obj.email = args[0], args[1] 
        elif "name" in kwargs and "email" in kwargs:
            obj.name, obj.email = kwargs["name"], kwargs["email"]

        # Check If An Equal Member Already Exists
        for mem in members_list:
            if mem == obj:
                return mem 
        
        # Otherwise Return Our Fresh Object
        return obj
    

    def __init__(self, name, email):
        # Initializing Inherited Attributes
        super().__init__(name, email)
        # Only initialize new members (existing ones already set)
        if not hasattr(self, 'id'):
            self.borrowed_books = []
            self.id = utils.get_id(10**6 + 1, 10**8)
            members_list.append(self)


    # Borrow Book From Our Books List If Available 
    # Adds Book To User Borrowed Books list
    def borrow_book(self, bok : book.Book):
        if bok in self.borrowed_books:
            print("You have a copy of this book")
        elif bok not in book.books_list:
            print("We don't have this book")
        else:
            if book.books_list[book.books_list.index(bok)].copies > 0:
                book.books_list[book.books_list.index(bok)].copies -= 1
                self.borrowed_books.append(bok)
            else:
                print(f"There are no available copies from {bok.title}")
    

    # Return The Borrowed Book And Remove It From User Borrowed Books
    def return_book(self, bok : book.Book): 
        if bok in book.books_list:
            book.books_list[book.books_list.index(bok)].copies += 1
        else:
            book.books_list.append(book.Book(bok.title, bok.author, 1))
        if bok in self.borrowed_books:
            self.borrowed_books.remove(bok)
        else:
            print("You didn't borrow this book")
    

    def __str__(self):
        return super().__str__() + f"\nID: {self.id} \nBorrowed Books: {self.borrowed_books}"
    

    def __eq__(self, other):
        if isinstance(other, Member):
            return self.name == other.name and self.email == other.email
        return False
        

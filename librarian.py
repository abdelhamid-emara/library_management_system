import baseclass, book, utils

# Used To Store All Employee When Program Runs
employees_list = []

# Librarian Class Inherits Person Class
class Librarian(baseclass.Person):
    def __new__(cls, *args, **kwargs):
        # Create Temporary Object Just To Compare
        obj = super().__new__(cls)
        if len(args) >= 2: 
            obj.name, obj.email = args[0], args[1] 
        elif "name" in kwargs and "email" in kwargs:
            obj.name, obj.email = kwargs["name"], kwargs["email"]

        # Check If An Equal Member Already Exists
        for emp in employees_list:
            if emp == obj:
                return emp 
        
        # Otherwise Return Our Fresh Object
        return obj
    

    def __init__(self, name, email):
        # Initializing Inherited Attributes
        super().__init__(name, email)
        # # Only initialize new members (existing ones already set)
        if not hasattr(self, 'id'):
            self.id =  utils.get_id(10**5 + 1, 10**6)
            employees_list.append(self)


    # Adds Book To Our Book List
    def add_book(self, bok : book.Book):
        if bok in book.books_list:
            book.books_list[book.books_list.index(bok)].copies += bok.copies
        else:
            book.books_list.append(bok)

    # Remove Book From Our Book List
    def remove_book(self, bok : book.Book):
        if bok in book.books_list:
            book.books_list.remove(bok)
        else:
            print(f"There are no {bok.title} in our book list")

    def __str__(self):
        return super().__str__() + f"\nID: {self.id}"
    
    def __eq__(self, other):
        if isinstance(other, Librarian):
            return self.name == other.name and self.email == other.email
        return False


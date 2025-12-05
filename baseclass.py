# Base Class Inherited By Librarian & Member Classes
class Person():
    def __init__(self, name : str, email : str):
        # Initialize Attributes 
        self.name = name.replace(" ", "").capitalize()
        self.email = email.replace(" ", "").lower()

    def __str__(self):
        return f"Name: {self.name} \nEmail: {self.email}"
    
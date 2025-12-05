from random import randint
import member, librarian, book

# Get Available ID
def get_id(frm, to) -> str:
    prefix = 'm_' if frm == (10**6 + 1) else 'e_'
    lis = member.members_list if frm == (10**6 + 1) else librarian.employees_list
    
    while True:
        the_id = prefix + str(randint(10**6 + 1, 10**8))
        flag = False
        for mem in lis:
            if mem.id == the_id:
                flag = True
        if not flag: break

    return the_id

# Check Non Repeated Element
def no_repeat(lis : list):
    unique = []
    for i in lis:
        if i not in unique:
            unique.append(i)
    return unique

# Show List Components
def show_info(lis : list):
    print('=' * 30)
    for i in lis:
        print(i)
        print ('*' * 20)
    print('=' * 30)

# Return Book
def make_book(user):
    title = input("Title: ") 
    author = input("Author: ") 
    copies = 1
    if isinstance(user, librarian.Librarian): copies = int(input("Copies: "))
    return book.Book(title, author, copies)

# Make Action
def make_mem_act(user):
    while True:
        x = 0
        while x not in [1, 2, 3, 4]:
            print('=' * 30)
            x = int(input("1- Borrow Book \n2- Return Book \n3- Show Books List \n4- end\n"))
        if x == 1:
            bo = make_book(user)
            user.borrow_book(bo)
        elif x == 2:
            bo = make_book(user)
            user.return_book(bo)
        elif x == 3:
            show_info(book.books_list)
        else: return
            

def make_lib_act(user):
    while True:
        x = 0
        while x not in [1, 2, 3, 4, 5, 6]:
            print('=' * 30)
            x = int(input("1- Add Book \n2- Remove Book \n3- Show Books List \n4- Show Members \n5- Show Librarians \n6- end\n"))
            if x in [1, 2, 3, 4, 5, 6]: break
        if x == 1:
            bo = make_book(user)
            user.add_book(bo)
        elif x == 2:
            bo = make_book(user)
            user.remove_book(bo)
        elif x == 3:
            show_info(book.books_list)
        elif x == 4:
            show_info(member.members_list)
        elif x == 5:
            show_info(librarian.employees_list)
        else: return

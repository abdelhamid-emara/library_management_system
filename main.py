import member, librarian, book, database, utils, login


# When The Program Starts => Access Data From Data Base
book.books_list = database.read_data_base(r"D:\library_management_system\db\books_data.txt")
member.members_list = database.read_data_base(r"D:\library_management_system\db\members_data.txt")
librarian.employees_list = database.read_data_base(r"D:\library_management_system\db\employees_data.txt")

cas = login.login()
user = 0

name = input("Enter your name: ")
email = input("Enter your email: ")

if cas == 1:    # Librarian Case
    user = librarian.Librarian(name, email)
    utils.no_repeat(librarian.employees_list)
    utils.make_lib_act(user)
else:           # Member Case  
    user = member.Member(name, email)
    utils.no_repeat(member.members_list)
    utils.make_mem_act(user)


# When The Program Ends => Update Data In Data Base
database.update_data_base(r"D:\library_management_system\db\books_data.txt", book.books_list)
database.update_data_base(r"D:\library_management_system\db\members_data.txt", member.members_list)
database.update_data_base(r"D:\library_management_system\db\employees_data.txt", librarian.employees_list)

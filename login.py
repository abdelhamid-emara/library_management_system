def login(x = 0):
    while True:
        print('=' * 30)
        print('=' * 9, "Login Page", '=' * 9)
        print('=' * 30)
        print("1- Librarian\n2- Member")
        x = int(input("Your Choice: "))
        if x in [1, 2]: break
    return x

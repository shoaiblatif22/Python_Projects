master_pwd = input("What is the master password? ")


def view():
    pass

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('password.txt', 'a') as f: #with automatically closes the file once used. 'a' appends the file and adds to the end of the existing file or creates a new file if file doesnt exist.
        f.write(name + "|" + pwd)


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        quit() 
        
name = input('Please enter your name: ')
if len(name) >= 6:
    if name[0] == 'E':
        print("My sister's name starts with E too!")
    elif name[0] == 'R':
        print("My husband's name starts with R too!")
    else:
        print("That's quite a long name!")
else:
    print("Your name is kind of short.")

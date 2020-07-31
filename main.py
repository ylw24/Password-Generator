import random
import string
import itertools

loop = True


def password():
    import random
    password = []
    password.append(GRN(n=5))
    password.append(GRL(l=3))
    password.append(GRS(s=2))
    password = list(itertools.chain.from_iterable(password))
    random.shuffle(password)
    password = ''.join(password)
    return password


def GRN(n):
    number = []
    for i in range(n):
        number.append(str(random.randint(1, 10)))
    return number


def GRL(l):
    letter = []
    for i in range(l):
        letter.append(random.choice(string.ascii_letters))
    return letter


def GRS(s):
    symbol = []
    for i in range(s):
        symbol.append(random.choice(string.punctuation))
    return symbol


while loop:
    print(" ")
    print("What password type would you like to generate?")
    print("a) standard 10-digit password with 5 numbers, 3 letters, 2 symbols.")
    print("b) I would like to choose how many numbers, letters, and symbols are contained in my password.")
    print("c) exit")
    print(" ")
    action = input()
    if action == 'a':
        print(password())
        print("\nWould you like another/different password?")
        repeat = input("Y/N \n")
        if repeat == 'Y':
            continue
        if repeat == 'N':
            break
    if action == 'b':
        print(" ")
        print("How many digits of the following would your password contain:")
        try:
            n = int(input("number?  "))
            l = int(input("Letter?  "))
            s = int(input("symbol?  "))
        except:
            print("Invalid Input: Please enter an integer (e.g. 7")
            continue
        dgt = int(n) + int(l) + int(s)
        print("Your password contain a total of " + str(dgt) + " digits")
        generateQ = input("Generate Password: Y/N   ")
        if generateQ == 'Y':
            print(password())
            print("\nWould you like another/different password?")
            repeat = input("Y/N \n")
            if repeat == 'Y':
                continue
            if repeat == 'N':
                break
        if generateQ == 'N':
            continue
    if action == 'c':
        break
    else:
        print("invalid input, please enter a letter. \n")
        continue

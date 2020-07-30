import random
import string
import itertools

loop = True


def password():
    import random
    password = []
    password.append(GRN())
    password.append(GRL())
    password.append(GRS())
    password = list(itertools.chain.from_iterable(password))
    random.shuffle(password)
    password = ''.join(password)
    return password


def GRN():
    number = []
    for i in range(5):
        number.append(str(random.randint(1, 10)))
    return number


def GRL():
    letter = []
    for i in range(3):
        letter.append(random.choice(string.ascii_letters))
    return letter


def GRS():
    symbol = []
    for i in range(2):
        symbol.append(random.choice(string.punctuation))
    return symbol


while loop:
    print("What password type would you like to generate?")
    print("a) standard 10-digit password")
    print("b) exit")
    action = input()
    if action == 'a':
        print(password())
        print("\nWould you like another/different password?")
        repeat = input("Y/N \n")
        if repeat == 'Y':
            print('')
            continue
        if repeat == 'N':
            break

    if action == 'b':
        break
    else:
        print("invalid input, please enter a letter. \n")
        continue

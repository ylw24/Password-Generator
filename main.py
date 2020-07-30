import random
import string
import itertools

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
        number.append(str(random.randint(1,10)))
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

while True:
    print("What password type would you like to generate?")
    print("a) standard 10-digit password")
    action = input()
    if action == 'a':
        print(password())
        break
    else:
        print("invalid input, please enter a letter.")
        continue

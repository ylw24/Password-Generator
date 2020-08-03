import random
import string
import itertools

loop = True
saved_passwords = []
#SP_file = open("saved_passwords", "r+")
#clear file
#SP_file.truncate(0)

split = lambda word: [char for char in word]
#def split(word):
#    return [char for char in word]

count=0
count = lambda num: num+1
#def count(letter):
#    return letter+=1

def password():
    import random
    password = []
    password.append(GRN(n=5))
    password.append(GRL(l=3))
    password.append(GRS(s=2))
    # get rid of all nested lists, converts them into one list
    password = list(itertools.chain.from_iterable(password))
    # shuffles the position of the items in the list
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


def customPASS(cnumbers, cletters, csymbols):
    megaPASS = []
    if cnumbers != None:
        megaPASS.append(split(cnumbers))
    if cletters != None:
        megaPASS.append(split(cletters))
    if csymbols != None:
        megaPASS.append(split(csymbols))
    megaPASS = list(itertools.chain.from_iterable(megaPASS))
    random.shuffle(megaPASS)
    megaPASS = ''.join(megaPASS)
    return megaPASS


while loop:
    print(" ")
    print("What password type would you like to generate?")
    print("a) standard 10-digit password with 5 numbers, 3 letters, 2 symbols.")
    print("b) I would like to choose HOW MANY numbers, letters, and symbols are contained in my password.")
    print("c) I would like to choose WHAT numbers, letters, and symbols are contained in my password.")
    print("d) exit")
    action = input()
    if action == 'a':
        thePASS = password()
        print(thePASS)
        print("\nWould you like to save this password to your list?")
        save = input("Y/N \n")
        if save == 'Y':
            saved_passwords.append(thePASS)
            # SP_file.write(thePASS)
            # SP_file.write('\n')
        elif save == 'N':
            pass
        print("\nWould you like another/different password?")
        repeat = input("Y/N \n")
        if repeat == 'Y':
            continue
        elif repeat == 'N':
            break
    elif action == 'b':
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
            thePASS = password()
            print(thePASS)
            print("\nWould you like to save this password to your list?")
            save = input("Y/N \n")
            if save == 'Y':
                saved_passwords.append(thePASS)
                #SP_file.write(thePASS)
                #SP_file.write('\n')
            elif save == 'N':
                pass
            print("\nWould you like another/different password?")
            repeat = input("Y/N \n")
            if repeat == 'Y':
                continue
            elif repeat == 'N':
                break
        elif generateQ == 'N':
            continue
    elif action == 'c':
        Act = input("Would you like to include custom numbers? Y/N")
        if Act == 'Y':
            cnumbers = input("Enter your number(s):  ")
        elif Act == 'N':
            cnumbers = None
            pass
        Act = input("Would you like to include custom letters Y/N")
        if Act == 'Y':
            cletters = input("Enter your letter(s):  ")
        elif Act == 'N':
            cletters = None
            pass
        Act = input("Would you like to include custom symbols? Y/N")
        if Act == 'Y':
            csymbols = input("Enter your symbol(s):  ")
        elif Act == 'N':
            csymbols = None
            pass
        thePASS = customPASS(cnumbers, cletters, csymbols)
        print(thePASS)
        print("\nWould you like to save this password to your list?")
        save = input("Y/N \n")
        if save == 'Y':
            saved_passwords.append(thePASS)
            # SP_file.write(thePASS)
            # SP_file.write('\n')
        elif save == 'N':
            pass
        print("\nWould you like another/different password?")
        repeat = input("Y/N \n")
        if repeat == 'Y':
            continue
        elif repeat == 'N':
            break
    elif action == 'd':
        break
    else:
        print("invalid input, please enter a letter. \n")
        continue

A = input('Would you like to view your saved password list? Y/N \n')
if A == 'Y':
    print(saved_passwords)
    #for element in SP_file:
    #    print(element)
elif A == 'N':
    print('Thanks for using the Password Generator')

import time
import random
import string

length = 10
specialCharacters = True
numbers = True
capitals = True
repeat = True


print('Welcome to Password Generator!')
time.sleep(1)

# pwd length
# need to create error for int(lengthTemp) [currently crashes program]
while repeat:
    lengthTemp = input('How long should you password be (Enter only numbers)? ')
    lengthInt = int(lengthTemp)
    if lengthInt < 1:
        print('Please enter a higher value!')
    elif lengthInt > 25:
        print('Please enter a lower value!')
    else:
        length = lengthInt
        repeat = False

repeat = True

# special characters
while repeat:
    userInput = input('Should your password include special characters [y/n]? ')
    if userInput == 'y':
        specialCharacters = True
        repeat = False
    elif userInput == 'n':
        specialCharacters = False
        repeat = False
    else:
        print('Please enter "y" or "n" only!')

repeat = True

# numbers
while repeat:
    userInput = input('Should your password include numbers [y/n]? ')
    if userInput == 'y':
        numbers = True
        repeat = False
    elif userInput == 'n':
        numbers = False
        repeat = False
    else:
        print('Please enter "y" or "n" only!')

repeat = True

# capitals
while repeat:
    userInput = input('Should your password include uppercase characters [y/n]? ')
    if userInput == 'y':
        capitals = True
        repeat = False
    elif userInput == 'n':
        capitals = False
        repeat = False
    else:
        print('Please enter "y" or "n" only!')

# 1 1 1
if specialCharacters & numbers & capitals:
    possibleCharacters = string.printable
    # problem: includes ' ' as a character
    pwd = ''.join(random.sample(possibleCharacters, length))
    print(pwd)

# 1 1 0
if specialCharacters & numbers & capitals == False:
    possibleCharacters1 = string.ascii_lowercase
    possibleCharacters2 = string.punctuation
    possibleCharacters3 = string.digits
    possibleCharacters = possibleCharacters1 + possibleCharacters2 + possibleCharacters3
    
    pwd = ''.join(random.sample(possibleCharacters, length))
    print(pwd)

# 1 0 1
if specialCharacters & numbers == False & capitals:
    # can make pc = string.punctutation + string.lowercase staightaway, making more efficient
    pc1 = string.punctuation
    pc2 = string.ascii_letters
    pc = pc1 + pc2

    pwd = ''.join(random.sample(pc, length))
    print(pwd)

# 1 0 0
if specialCharacters & numbers == False & capitals == False:
    pc1 = string.ascii_lowercase
    pc2 = string.punctuation
    pc = pc1 + pc2

    pwd = ''.join(random.sample(pc, length))
    print(pwd)

# 0 1 1
if specialCharacters == False & numbers & capitals:
    pc1 = string.ascii_letters
    pc2 = string.digits
    pc = pc1 + pc2

    pwd = ''.join(random.sample(pc, length))
    print(pwd)

# 0 1 0
if specialCharacters == False & numbers& capitals == False:
    pc1 = string.ascii_lowercase
    pc2 = string.digits
    pc = pc1 + pc2

    pwd = ''.join(random.sample(pc, length))
    print(pwd)

# 0 0 1
if specialCharacters == False & numbers == False & capitals:
    pc = string.ascii_letters

    pwd = ''.join(random.sample(pc, length))
    print(pwd)

# 0 0 0
if specialCharacters == False & numbers == False & capitals == False:
    pwd = ''.join(random.sample(string.ascii_lowercase, length))
    print(pwd)

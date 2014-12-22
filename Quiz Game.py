print('''Welcome to The Quiz game!
''')
def q1():
    print('Who made minecraft?')
    answer = input('>')
    if answer.lower() == "Markus Perrson":
        print('Correct! You must be a minecrafter!')
        return 4
    elif 'Notch' in answer:
            print('Close, but not really!')
            return 2
    else:
        return 0
def q2():
    print('What is rob`s middle name?')
    answer = input('>')
    if answer.lower() == "Sterling":
        print('Correct! #Skilstak!')
        return 4
    elif 'Muhlestein' in answer:
        print('Close, but not really!')
        return 2
    else:
        return 0

def q3():
    print('Do you like waffles? (Trick Question)')
    answer = input('>')
    if answer.lower() == "Yes":
        print('Correct! I like waffles!')
        return 4
    elif 'No' in answer:
        print('Close, but no')
        return 2
    else:
        return 0

def q4():
    print('What is 107 x 7?')
    answer = input('>')
    if answer.lower() == "749":
        print('Correct! You are smart')

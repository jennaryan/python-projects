
def ask(question):
    answer = input(question)
    answer = answer.lower().strip()
    print("Thou hast answered: " + answer)
    return answer

def ask_color():
    return ask("What is your favorite color?")

#---------------------------------------------------------------------

print('''
Who would cross the Bridge of Death must answer me these questions three ...
''')

name = ask("What is your name? ")
quest = ask("What is your quest? ")

if name.startswith('lancelot'):
     color = ask("What is your favorite color? ")
elif name.startswith('robin'):
    capital = ask("What is the capital of Assyria?")
elif name.startswith('galahad'):
    color = ask_color()
else:
    print("You aren't in the movie. Go away. NOW!")

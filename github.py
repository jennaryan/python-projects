import random

answers = ['yes','no','maybe','totally','mhm','ask me again later','why bother','why should you','go ahead','NO SHUT UP','eh not in the mood to answer','alright friend','keep dreaming','you suck','i dont care','pickles' ]

while True:
    print('What is your question?')
    question = input('> ')
    if 'die' in question:
        print("I am sorry, i don't deal with mortality.")
    elif 'love' in question:
        print("......Uhh.....ask someone else.....love is good though")
    elif 'you' in question:
        print("Don't talk about my booty!")
    else:    
        answer = random.choice(answers)
        print(answer)


  

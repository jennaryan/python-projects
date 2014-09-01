import random

answers = ['yes','no','yeah','go ahead','maybe','sure','keep dreaming','follow your dreams','im not in the mood to answer','WAFFLES!','totally bruh','alright baby']


while True:
    print("Ask me a question")
    question = input('> ')
    if 'die' in question:
        print("I don't deal with mortality")
    elif 'love' in question:
        print("I don't deal with your love life")
    elif 'pickles' in question:
        print("PICKLES!")
    else:
        answer = random.choice(answers)
        print(answer)


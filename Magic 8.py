import random

answer = ['Yes','no','maybe','i dont feel like talking right now','Hi','Idk']

while True:
    question = input("What is your question?").lower().strip()
    if 'die' in question:
        print("I don't deal with mortality")
    elif 'love' in question:
        print("I don't deal with your love life")
    elif 'pickles' in question:
        print("I like pickles")
    else:
        random = random.choice(answer)
        print(random)

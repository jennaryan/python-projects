import random
import time
answers = ['yes','no','maybe','in your dreams','ask me later','whateves',]

while True:
    time.sleep(1)
    question = input('What is your question?').lower().strip()
    time.sleep(1)
    if 'die' in question:
        print("I don't deal with mortality")
    elif 'love' in question:
        print("I don't deal with dat drama")
    elif 'waffles' in question:
        print("Mhm i like waffles")
    else:
        answer = random.choice(answers)
        print(answer)
    

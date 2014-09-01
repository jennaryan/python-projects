import time



rewards = [
    {
        'name': "Regular Attendance",
        'desc': "One regular class (92-120 mins)",
        'min': 40,
        'max': 40,
    },
    {
        'name': "GitHub Green Dot",
        'desc': "Get a green dot from committing something new",
        'min': 10,
        'max': 40,
    }    
]

items = [
    {
    'name': "Tee Shirt (Basic)",
    'desc': "The basic SkilStak logo on a tee shirt (whatever size).",
    'cost': 600
    },
    {
        'name': "Saturday Minecraft Camp",
        'desc': "Regular 2-hour Minecraft camp held Saturdays (usually 3-5)",
        'cost': 400
    },
    {
        'name': "Water Bottle",
        'desc': "One of our regular water bottles with SkilStak logo",
        'cost': 150
    },

]
print("Rewards:")
time.sleep(0.5)
for reward in rewards:
    if reward['min'] == reward['max']:
        print("{name}: {min}".format(**reward))
    else:    
        print("{name}: {min}-{max}".format(**reward))
time.sleep(1)
print("Items:")
time.sleep(0.5)
for item in items:
    print("Item: {name}. Description: {desc}. Cost: {cost}".format(**item))
    
          

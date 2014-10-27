import time

buxperclass = 2
buxpergreendot = 1
buxperport = 2
buxperhourofwork = 10
buxpercodeorg = 30


classes = input("How many classes have you done?")
classes = int(classes)
print(classes * 2 )
time.sleep(2)
greendot = input("How many greendots do you have?")
greendot = int(greendot)
print(greendot * 1)
time.sleep(2)
port = input("How many ports have you done?")
port = int(port)
print(port * 2)
time.sleep(2)
how = input("How many hours of work have you done (skilstak admins only!)?")
how = int(how)
print(how * 10)
time.sleep(2)
finishcodeorg = input("Have you finished code.org yet?").lower().strip()
if finishcodeorg == 'yes':
    print("30")
    time.sleep(2)
    print("Calculating total... total is....")
    time.sleep(3)
    print(classes + greendot + port + how + 30)
elif finishcodeorg == 'no':
    print("Finish it! But here is the total....")
    time.sleep(3)
    print(classes + greendot + port + how)
else:
    print("WHHAA?????")
    time.sleep(0.5)
    print("I don't speak that... whatever it is. Please start over, but put in 'yes' or 'no'")

    



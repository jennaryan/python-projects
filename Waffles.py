import time

yeah = ('yes','yeah','yup','totally','mhm','yus')
        



waffles = input("Do you like waffles? ").lower().strip()
        
if waffles.startswith(yeah):
    print("Yeah we like waffles! ")
    pancakes = input("Do you like pancakes? ").lower().strip()
    if pancakes.startswith(yeah):
        print("Yeah we like pancakes! ")
        french_toast = input("Do you like french toast? ").lower().strip()
        if french_toast.startswith(yeah):
            print("Doo doo doo doooo, can't wait to get a mouthful! ")
            time.sleep(1)
            print("WAFFLES! ")
            time.sleep(2)
            print("WAFFLES! ")
            time.sleep(2)
            print("WAFFLES! ")
            time.sleep(2)
waffles = input("Do you like waffles? ").lower().strip()
        
if waffles.startswith(yeah):
    print("Yeah we like waffles! ")
    pancakes = input("Do you like pancakes? ").lower().strip()
    if pancakes.startswith(yeah):
        print("Yeah we like pancakes! ")
        french_toast = input("Do you like french toast? ").lower().strip()
        if french_toast.startswith(yeah):
            print("Doo doo doo doooo, can't wait to get a mouthful! ")                        
        
else:
    print("GO SIT IN A CORNER AND THINK ABOUT WHAT YOU HAVE SAID")


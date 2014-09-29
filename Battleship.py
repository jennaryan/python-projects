class Ship:
    size = None
    
    def __init__(self):
        self.front = None
        self.back = None
        self.destroyed = False

    def pace(self,front,back):
        self.front = front
        self.back = back

class Carrier(Ship):
    size = 5
    
class Battleship(Ship):
    size = 4

class Submarine(Ship):
    size = 3

class Destroyer(Ship):
    size = 3

class PatrolBoat(Ship):
    size = 2

my_carrier = Carrier()
comp_carrier = Carrier()

front_row = 'z'
while front_row not in 'abcdefghij':
    front_row= input('Carrier Front Row [a-j]:')
    
front_col = 0
while not front_col > 1 or front_col <=10:
    front_col = int(input('Carrier Front Colomn [1-10]:'))
print(front_row,front_col)

back = input('Carrier Back:')

my_carrier.front = front
my_carrier.back = back





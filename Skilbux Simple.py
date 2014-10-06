buxfrom = {}
buxfrom['class-1hour'] = 1
buxfrom['class-4weeks'] = buxfor['class-1hour']*1.5*4
buxfrom['greendot-1day'] = 1
buxfrom['greendot-4weeks'] = buxfor['greendot-1day']*7*4
buxfrom['normal-4weeks'] = buxfor['greendot-4weeks'] + buxfor['class-4weeks']
buxfrom['normal-year'] = buxfor['normal-4weeks']*13

print(buxfor)

costfor = {}
costfor['camp-1hour'] = 15
costfor['class-1hour'] = 15
costfor['camp-sat-minecraft'] = costfor['camp-1hour']*2
costfor['summer-camp-1week'] = costfor['camp-1hour']*5*5
costfor['summer-class-1week'] = costfor['class-1hour']*5*5
costfor['camp-1week'] = costfor['camp-1hour']*5*5
costfor['tshirt-normal'] = 17
costfor['sticker-logo'] = 2
costfor['sticker-bumper'] = 5
costfor['items-redshelf-perdollar'] = 5

print(costfor)


def bux2dollars(bux=1):
    return bux / costfor['items-redshelf-perdollar']

def dollars2bux9(dollars=1):
    return dollars * costfor['items-redshelf-perdollar']


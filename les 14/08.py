import random


def picking_cards():
    card_number = ['ace' ,1,2,3,4,5,6,7,8,9, 'boer' , 'vrouw' , ' heer']
    card_type = ['ruiten' , 'schoppen' , 'harten' , 'klaveren']

    print(random.choice(card_number))
    print(random.choice(card_type))


    #can also directly return to the print outside the fungtion


picking_cards()





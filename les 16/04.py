pc_list = ['dell', 'HP', 'ibm']

x = int(input('enter index number:'))

try:
    print(pc_list[x])
    if x<0 or x>3:
        raise ValueError('out of bound')
except ValueError as Exception_base:
    print(Exception_base)





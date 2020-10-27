x1 ="30"
x2 = 10


try:
    x1/x2
except TypeError as E1:
    print(E1)






list = [3,1,6,9]
try:
    print(list[8])
except TypeError as E2:
    print('error on the list requested item does not exist')






ui = (input("voer getal in tussen (1/3) :"))
sa = '2'

if ui.isdigit() == False:
    print('voer aleen nummers in')
elif ui < sa:
    print('too low')
elif ui > sa:
    print('too high')
else:
    print('you are correct')


#print(type(ui))
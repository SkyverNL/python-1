menu = ('Vlees,Groente,Pasta')

print("menu:" + menu)

bestelling = input('kies u gerecht:')

if bestelling.lower() in menu.lower():
    print (bestelling +': staat op menu')
else:
    print(bestelling +': besteling niet op menu')

def compare(a,b,c):
    if a > b and a > c :
        return a
    elif b > a and b > c:
        return b
    elif c > b and c > a :
        return c
    else:
        print('fucking error')

15




var1 = int(input('voer eerste nummer in :'))
var2 = int(input('voer 2e nummer in :'))
var3 = int(input('voer 3e nummer in :'))


solution = compare(var1,var2,var3)

print(f'{solution}')

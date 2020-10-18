getal1 = int(input('voer 1e getal in:'))
getal2 = int(input('voer 1e getal in:'))
getal3 = int(input('voer 1e getal in:'))

bignum = 0

if getal1 > getal2 and getal2 < getal3:
    bignum = 1
elif getal2 > getal3 and getal3 < getal1:
        bignum = 2
elif getal3 > getal1 and getal1 < getal2:
            bignum = 3
else:print("incorecte invoer")




print(f'getal{bignum} is het grootste:')
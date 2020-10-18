naam = input('voer naam in :')
cijfer= int(input('voer cijfer in :'))


if cijfer <= 5:
    print(f'{naam},s cijfer is onvoldoende')
elif cijfer >= 6 and cijfer <= 8:
    print(f'{naam},s cijfer is voldoende')
else:
    print(f'{naam},s cijfer is goed')
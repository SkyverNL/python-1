info = ['init']
info.append(1)
info.append(2)
info.append(3)

info[1] = input('voer naam in:')
info[2] = int(input('voer leeftijd in:'))
info[3] = int(input('voer lengte in:'))

if info[2] >= 16 and info[2] <= 30 and info[3] >= 180:
    print(f'{info[1]} is geselecteerd ')
else:
    print(input(f'{info[1]} is niet geselecteerd '))























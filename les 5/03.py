spreekwoord = ('Als de blinde de ander leidt vallen ze beiden in de gracht ')

print(f'{spreekwoord}')

zoek = input('voer zoekwoord in : ')


if zoek.lower() in spreekwoord.lower():
    print('woord gevonden')
else:
    print('woord niet gevonden')
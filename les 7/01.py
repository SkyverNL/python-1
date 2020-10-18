def calc(dollar):

    euro = dollar/1.20

    return euro

dollar = float(input('voer bedrag in : '))

euro = calc(dollar)

print(f'het bedrag in euro is %.2f' % euro )
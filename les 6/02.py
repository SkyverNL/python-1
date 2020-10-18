
bruto = float(input('bruto : '))
belasting_tarief = float(input('belasting tarief : '))


def bereken_netto_salaris(bruto, belasting_tarief):
    belasting = bruto * belasting_tarief
    netto = bruto - belasting
    print(f'{netto}')
    #return netto


bereken_netto_salaris(bruto,belasting_tarief)

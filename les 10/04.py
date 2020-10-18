
def gold_calc():
    priceG = float(input('goldprice:'))
    priceS = float(input('silverPrice:'))
    budget = float(input('input budget:'))

    resultG = budget  / priceG
    resultS = budget  / priceS

    print(f'you can buy {resultG} ounces of gold' '\n' f'you can buy {resultS} ounces of silver ' )

gold_calc()


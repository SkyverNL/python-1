prijs = int(input('voer prijs in:'))
leeftijd = int(input('voer leeftijd in :'))


if leeftijd <= 10 or leeftijd >= 60:
    prijs -= prijs * 0.50
else:
    prijs -= prijs * 0.10
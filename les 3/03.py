kaartprijs = int(input('wat is prijs van kaartje?:'))
aantalP = int(input('hoeveel reizgers?:'))
jongste = int(input('hoe oud is de jongste?:'))

korting1 = kaartprijs * 0.20
korting2 = kaartprijs * 0.10


if aantalP >= 5:
    kaartprijs = kaartprijs - korting1

if jongste <= 12:
    kaartprijs = kaartprijs - korting2

print(f'de kaartprijs is {kaartprijs}')
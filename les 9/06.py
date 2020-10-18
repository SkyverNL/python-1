import time
def check_anwser(Q,A ):
   if Q == A:
       return True
   else:
       return False

A1 = "B"

A2 = "D"


Q1 = input(f"welk auto merk is de eigenaar van lamborgini?\n\n" "is dat" "\n" "A: bmw" "\n" "B: audi" "\n" "C: Volkswagen" 
           "\n" "D: fiat" "\n" "voer antwoord in:")


if check_anwser(Q1.upper() ,A1):
    print("correct" "\n" "u heeft 1 antwoorden goed")
    time.sleep(4)
    print('\n' * 100)

    Q2 = input(
        f"wie is de rijkste man op aarde\n\n" "is dat" "\n\n" "A: billgates" "\n" "B: elon musk" "\n" "C: john kennedy"
        "\n" "D: jeff bezos" "\n" "voer antwoord in:")

    if check_anwser(Q2.upper(), A2):
        print('\n' 'correct' '\n\n' 'u heeft 2 antwoorden goed')
        time.sleep(4)
        print('\n' * 100)
    else:
        print('incorect u verliest u heeft een Smoll PP')
else:
    print('incorect u verliest u heeft een Smoll PP')


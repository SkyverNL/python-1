valid = False

while not valid:
    try:
        x = int(input('enter a number between 1 & 10'))
        if x<1 or x>10:
            raise ValueError("not in acceptable range")
        valid = True
    except ValueError as Exception_base:
        print(Exception_base)
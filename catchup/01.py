cars = 0
all_cars = " "


while cars <= 4:
    car = input(f"input car name :")
    all_cars = all_cars + car +  " "
    cars = cars + 1
else:
    print(f"all the cars are\n{all_cars}")


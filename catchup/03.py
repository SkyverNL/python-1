import os
map = "C:\\python_map\\"



#os.mkdir(map)   #make dir

#os.rmdir(map)   #remove dir

def main():
    i = 0

    while i < 100 :
        f = open(f"{map}{i}.txt","w+")
        f.write(f"this is number-{i}")
        f.close()
        i = i + 1
        print(i)
    else:
        pass


pas = False

ui = int(input("about to create 100 files \nenter 1 to contine\n"))


if ui == 1:
    pas = True


if pas:
    main()
else:
    print("failed")

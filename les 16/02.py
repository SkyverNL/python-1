list1 = [2,5,6,8]
list2 = [8,5,9,8]

for i in range(4):
    try:
        x = list1[i]/list2[i]
        print(x)

    except TypeError:
        print('wrong input')
    except ZeroDivisionError:
        print('can,t divide by 0')
    except Exception as exeption_object:
        print('unexpected error')
    else:
        print('no error found')
    finally:
        print('end of debug')


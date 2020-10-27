import os
map = "C:\\python_map\\"



if os.path.exists(map):
    print('file exist')
else:
    print('file found')
    try:
        os.remove(map)
        print("removed")
    except FileNotFoundError as fnfe_object:
        print(fnfe_object)
    except PermissionError as pe_object:
        print(pe_object)
    except Exception as ee_object:
        print(f'unexpected error trown' , ee_object)

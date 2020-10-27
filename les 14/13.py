from datetime import time



t = time(hour=20, minute=15)



format1 = t.strftime('%h:%m:%s')


print(format1)
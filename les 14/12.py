from datetime import datetime as DT

dt = DT.today()

t = dt.time()

d = dt.date()


dt_combine = dt.combine(date=d, time=t)

print(dt_combine)
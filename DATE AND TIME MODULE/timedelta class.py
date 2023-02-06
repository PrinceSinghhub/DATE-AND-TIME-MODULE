from datetime import *
td=timedelta(days=10)
print(td)
print("go to 10 day forword at present time")
d=date.today()
r=td+d
print(r)
print("go to 10 day backword at present time")
td=timedelta(days=-10,weeks=1)
d=date.today()
r=d-td
print(r)

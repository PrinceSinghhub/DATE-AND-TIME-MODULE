from datetime import *
# todo for our given data print
dt = datetime(year = 2021,month = 7,day = 30)
print(dt)
dt1 = datetime(year = 2021,month = 7,day = 30,hour=15,minute=40,second=56,microsecond=3500)
print(dt1)
# todo without date year only by data
dt2 = datetime(2021,7,30,15,40,56,173500)
print(dt2)
print("Excess data by usining attributes of datetime")
print(dt1.year)
print(dt1.month)
print(dt1.day)
print(dt1.hour)
print(dt1.minute)
print(dt1.second)
print(dt1.microsecond)


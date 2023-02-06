from datetime import *
Day=int(input("Enter Your Day: "))
Month=int(input("Enter Your Month: "))
Year=int(input("Enter Your Year: "))
dt = date(Year,Month,Day)
r=date.today()
year = dt.year
year1 = r.year
fy=year1-year
month = dt.month
month1 = r.month
fm=month1-month
day=dt.day
day1=r.day
fd=day1-day
print("**********************************")
print("           Your Age is        ")
print(f"Day: {fd} Month: {fm} Year: {fy}")
from time import *
epoch = time()
# todo return time in second
print(epoch)
print()

# todo convert date and time by using epoch
dt = ctime(epoch)
print(dt)
print()

# todo without parameter ctime()
print(ctime())
print()

# todo usining localtime()
local = localtime()
# todo print all details of today in formate of localtime()
print(local)
print("Excess data by using attributes")
print("year is:",local.tm_year)
print("current month is:",local.tm_mon)
print("day in month is:",local.tm_mday)
print("present hourse is:",local.tm_hour)
print("present min is:",local.tm_min)
print("present sec is:",local.tm_sec)
print("present week day is (mon is 0 here):",local.tm_wday)
print("present year day out of 365 is:",local.tm_yday)
print("our time zone name is:",local.tm_zone)
print("GMT UTC(cordinate universal time):",local.tm_gmtoff)
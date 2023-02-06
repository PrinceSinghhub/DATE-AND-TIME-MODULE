from time import *
# todo usining localtime()
local = localtime()
# todo print all details of today in formate of localtime()
print("IND standared time ny using localtime method")
print("our time zone name is:",local.tm_zone)
print("present hourse is:",local.tm_hour,end=":")
print("present min is:",local.tm_min,end=":")
print("present sec is:",local.tm_sec)
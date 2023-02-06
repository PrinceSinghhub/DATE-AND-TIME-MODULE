from datetime import *
d1=date(year=2021,month=5,day=13)
d2=date.today()
a=d1==d2
b=d1>d2
c=d1<d2
d=d1!=d2
print(f"d1==d2: {a}\nd1>d2: {b}\nd1<d2: {c}\nd1!=d2: {d}")
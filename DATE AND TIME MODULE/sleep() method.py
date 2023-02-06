# todo sleep method is used to stop our programe for few time
import time
def num(n):
    for i in range(n):
        print(i)
        if i==5:
            time.sleep(5)
num(10)

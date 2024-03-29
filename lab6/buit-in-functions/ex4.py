import time
import math

def delay(d, n):
    time.sleep(d)
    print(math.sqrt(n))

n = int(input("Your number: "))
d = int(input("Delay: "))
delay(d, n)
from math import *
def euler(n):
    n -= 1
    res = 0
    res += 3*floor(n/3)*(floor(n/3)+1)/2
    res += 5*floor(n/5)*(floor(n/5)+1)/2
    res -= 15*floor(n/15)*(floor(n/15)+1)/2
    print(res)

euler(1000)

# 233168
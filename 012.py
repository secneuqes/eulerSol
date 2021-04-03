# for a in range(20):
#     print(2*a+1) # -> 1 ~ 39
import math

def euler(k):
    res = 0
    
    for a in range(1,k):
        _sum_ = a*(a+1) / 2
        b_arr = prime_num_list(math.ceil(math.sqrt(_sum_)))
        li_soin_sep = []
        for each in b_arr:
            if _sum_ // each != 0:
                li_soin_sep.append([each, prime_num_n(_sum_,each)])
        pper = 1
        for each in li_soin_sep:
            if each[1] != 0:
                pper *= each[1] + 1

        print(pper)
        if pper >= 500:
            res = _sum_
            break
    return res

# 소수 n 개 구하는 함수
def prime_num_list(n): # n에는 prime 수의 개수
    prime = []
    p = 2

    while True:
        flag = 1
        if p % 2 == 0 and p != 2:
            flag = 0
        if flag  == 1:
            for each in prime:
                if p % each == 0:
                    flag = 0
            if flag == 1:
                prime.append(p)
        if prime[len(prime)-1] >= n:
            break
        p+=1

    return prime # prime list 반환

# p중 소인수 q가 몇개? -> k개 리턴
def prime_num_n(p, q):
    k = 0
    while True:
        if p % q == 0:
            k += 1
            p = p / q
        else:
            break
    return k

print(euler(50000))

# 76576500
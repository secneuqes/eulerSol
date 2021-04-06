import math
import timeit

start = timeit.default_timer()

def euler(n):
    arr_abnum = abNum(n)
    arr_succ = set(range(n))
    a = 0

    while a <= len(arr_abnum)-1:
        b = 0
        while b <= a and arr_abnum[a]+arr_abnum[b] < n:
            try:
                arr_succ.remove(arr_abnum[a]+arr_abnum[b])
                b += 1
            except:
                b += 1
        a += 1

    return sum(arr_succ)

def abNum(n):
    res = []
    # n 이하의 과잉수의 갯수 구하기
    for k in range(1,n+1):
        flagN = 0
        divArr = nDivisors(k)
        divArr.remove(k)
        flagN = sum(divArr)
        if flagN > k:
            # 이 경우 과잉수라고 할 수 있다.
            res.append(k)
    return res

def nDivisors(n):
    res = []
    # n의 제수를 반환 -> divisors(36) -> [1,2,3,4,6,9,12,18,36]
    for p in range(1,math.ceil(math.sqrt(n))+1):
        if n % p == 0:
            res.append(int(p))
            res.append(int(n/p))
    res = list(set(res))
    # res.sort()
    return res

print(euler(28123))

stop = timeit.default_timer()

print('Time: ', stop - start)

# 4179871
import math

def nPrime(n):
    # 
    start = 2
    count = 0
    while True:
        if all([start % i for i in range(2, int(math.sqrt(start)) + 1)]) != 0:
            count += 1
            if count == n:
                return start
        start += 1 

def pList(n):
    # n 까지의 소수 리스트 반환
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
    return prime

def nDivisors(n):
    res = []
    # n의 제수를 반환 -> divisors(36) -> [1,2,3,4,6,9,12,18,36]
    for p in range(1,math.ceil(math.sqrt(n))+1):
        if n % p == 0:
            res.append(int(p))
            res.append(int(n/p))
    res = list(set(res))
    res.sort()
    return res

def factors(n):
    # n 소인수 분해 -> factors(36) = [2,2,3,3]
    res=[]
    while n % 2 == 0:
        res.append(2),
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            res.append(i),
            n = n / i
    if n > 2:
        res.append(n)
    return res

def nFactorial(n):
    # n!
    return n * nFactorial(n-1) if n > 1 else 1

def fibo(n):
    # 피보나치 n번째 수
    if n <= 2: return 1
    else: return fibo(n-2) + fibo(n-1)

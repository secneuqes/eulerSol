def fibo(n):
    if n <= 2: return 1
    else: return fibo(n-2) + fibo(n-1)

def euler(n):
    res=0
    i=1
    while fibo(i)<n:
        if fibo(i)%2==0:
            res += fibo(i)
        i+=1
    print(res)

euler(4000000)

# 4613732
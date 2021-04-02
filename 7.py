def euler():
    prime = []
    p = 2
    while True:
        flag = 1
        for each in prime:
            if p % each == 0:
                flag = 0
        if flag == 1:
            prime.append(p)
            print(p)

        if len(prime) == 10001:
            print(prime[10000])
            break
        p+=1

euler()

# 104743
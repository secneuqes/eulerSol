res = 0

def euler():
    global res
    prime = []
    p = 2
    while True:
        flag = 1
        for each in prime:
            if p % each == 0:
                flag = 0
                break
        if flag == 1:
            prime.append(p)
            print(p)
        p+=1

        if p > 2000000:
            break
    
    for each in prime:
        res += each
    print(res)

euler()
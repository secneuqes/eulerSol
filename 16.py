res = 0

def euler(p,q):
    global res
    t = pow(p,q)
    k = list(str(t))
    for each in k:
        res += int(each)

    print(res)

euler(2,1000)

# 1366
# define euler function

def euler():
    sqsumres = 0
    res = 0
    sumto = (100*101)/2
    sumsq = pow(sumto, 2)

    for n in range(100):
        print(n+1)
        sqsumres += pow(n+1,2)

    res = sumsq - sqsumres

    print(res)

euler()

# 25164150
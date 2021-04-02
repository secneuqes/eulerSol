import timeit

start = timeit.default_timer()

max_res = 0
max_res_num = 0

def euler(n):
    global max_res
    for x in range(1,n+1):
        t = lenov(x)
        if t > max_res:
            max_res = t
            max_res_num = x
    print('result: ', max_res, max_res_num)

def lenov(k):
    len_lenov = 1
    while True:
        # print(k)
        if k % 2 == 0:
            k = k / 2
        else:
            k = 3*k + 1

        len_lenov += 1
        if k == 1:
            break

        

    return len_lenov

euler(1000000)


stop = timeit.default_timer()

print('Time: ', stop - start)  

# 837799
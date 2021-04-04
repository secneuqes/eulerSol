import math

def euler(n):
    res_final = []
    f_res_final = []
    res_sum = 0
    for t in range(1, n+1):
        preo = divarr(t)
        pret = divarr(preo)
        if t == pret and preo != pret:
            res_final.append(t)
            res_final.append(preo)
    # for each in res_final:
    #     if each not in f_res_final:
    #         f_res_final.append(each)
    f_res_final = list(set(res_final))
    f_res_final.sort()
    # print(f_res_final)
    for each in f_res_final:
        res_sum += each
    print(res_sum)


def divarr(k):
    arr_divisors = []
    res_arr = []
    res = 0
    for p in range(1,math.ceil(k//2)+1):
        if k % p == 0:
            arr_divisors.append(p)
            arr_divisors.append(k//p)
    # for each in arr_divisors:
    #     if each not in res_arr:
    #         res_arr.append(each)
    res_arr = list(set(arr_divisors))

    res_arr.sort()
    if res_arr:
        res_arr.remove(k)

    for each in res_arr:
        res += each

    return res

euler(10000)

# 31626
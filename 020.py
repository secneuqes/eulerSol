def factorial_recursive(n):
    return n * factorial_recursive(n-1) if n > 1 else 1

def euler(k):
    res = 0
    res_arr = list(str(factorial_recursive(k)))

    for each in res_arr:
        res += int(each)

    print(res)

euler(100)

# 648
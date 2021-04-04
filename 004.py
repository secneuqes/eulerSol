def euler():
    max_res = 0
    for x in range(100,1000):
        for y in range(100,1000):
            t = list(str(x * y))
            re_t = list(reversed(t))
            # print(t[:3],',',re_t[:3])
            if t[:3] == re_t[:3] and int(''.join(t)) > max_res:
                max_res = int(''.join(t))
    print(max_res)

euler()

# 906609
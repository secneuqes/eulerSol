res = []
res_fin = 0

def euler():
    global res, res_fin
    for a in range(1,500):
        for b in range(1,500):
            for c in range(1,500):
                if pow(a,2) + pow(b,2) == pow(c,2):
                    res.append([a,b,c])
                    # print(a,b,c)
    for each in res:
        if each[0] + each[1] + each[2] == 1000:
            print(each)
            res_fin = each[0] * each[1] * each[2]

euler()
print(res_fin)

# 31875000

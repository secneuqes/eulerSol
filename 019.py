def findoutplus(a,b):
    thirtyone = [1,3,5,7,8,10,12]
    for each in thirtyone:
        if each == b:
            return 31
    if a % 4 == 0 and a % 200 != 0:
        if b == 2: return 29
        else: return 30    
    else:
        if b == 2: return 28
        else: return 30 

def euler():
    f_day = 7
    res = 0

    for year in range(1900,2000):
        for month in range(1,13):
            yM = findoutplus(year, month)
            while f_day <= yM + 7:
                if f_day > yM:
                    f_day -= yM
                    break
                f_day += 7
            if f_day == 1:
                res += 1
    
    print(res)

euler()
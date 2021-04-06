from utils import *

def euler(n):
    res = 0
    arr_adnum = abNum(n)
    arr_succ = []

    for a in range(len(arr_adnum)-1):
        for b in range(len(arr_adnum)-1):
            arr_succ.append(arr_adnum[a]+arr_adnum[b])

    arr_succ = list(set(arr_succ))
    # arr_succ.sort()
    
    for l in range(1,n+1):
        if l not in arr_succ:
            res += l
            
    return res

def abNum(n):
    res = []
    # n 이하의 과잉수의 갯수 구하기
    for k in range(1,n+1):
        flagN = 0
        divArr = nDivisors(k)
        divArr.remove(k)
        for each in divArr:
            flagN += int(each)
        if flagN > k:
            # 이 경우 과잉수라고 할 수 있다.
            res.append(k)
    return res

print(euler(28123))
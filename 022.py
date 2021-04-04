listAlpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def euler():
    # 파일 열기
    f = open("./p_files/p022_names.txt", 'r')

    nameArr = list(f.read().replace('\"', '').split(','))
    s_nameArr = list(sorted(nameArr))

    nameCountArr = []
    for each in s_nameArr:
        t = 0
        for alpha in list(each):
            t += listAlpha.index(alpha) + 1
        nameCountArr.append(t)
    
    res = 0
    for x in range(len(s_nameArr)):
        res += (x+1) * nameCountArr[x]
    #파일 닫기
    f.close()
    print(res)
    
euler()

# 871198282
tri_str = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def choose(a,b):
    if a>b: return a
    elif a<b: return b
    else: return a

def euler():
    # 삼각형 열을 각각의 이차 배열로 생성
    tri_arr = tri_str.split('\n')
    while True:
        try:
            t = tri_arr[0].split()
            tri_arr.remove(tri_arr[0])
            tri_arr.append(t)
        except:
            break

    # 알고리즘에 따라 동작하게 생성
    
    # 알고리즘 설명
    # 삼각형의 가장 아래와 그 전의 줄의 수를 더했을때 더욱 큰 값을 갖는 쪽을 선택하여 올라간다. -> 이때 마지막 까지 실행하여 두수가 남는데 이중 큰 수 선택

    reverseTri = list(reversed(tri_arr))
    resForEach = []
    res = []
    for x in range(len(reverseTri)-1): # 각 열을 돌아가며 비교
        for y in range(len(reverseTri[x])-1):
            sim1 = int(reverseTri[x][y]) + int(reverseTri[x+1][y])
            sim2 = int(reverseTri[x][y+1]) + int(reverseTri[x+1][y])
            resForEach.append(choose(sim1, sim2))
        reverseTri[x+1] = resForEach
        resForEach = []
    return reverseTri[len(reverseTri)-1]

print(euler())

# 1074
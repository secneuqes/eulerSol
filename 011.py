# 문제에 주어진 20-20 배열 -> ['08', '02', ... , '50', '77', '91', '08']

str="""08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

arr=[]
for e in str.split('\n'):
    arr.append(e.split(' '))

# var 정의
max_horz = 0
max_horz_arr = []
max_vert = 0
max_vert_arr = []
max_diag_rd = 0
max_diag_rd_arr = []
max_diag_ld = 0
max_diag_ld_arr = []
# euler function

def euler():
    # 전역 함수 지정
    global max_horz, max_vert, max_diag_rd, max_diag_ld, max_horz_arr, max_vert_arr, max_diag_rd_arr, max_diag_ld_arr

    # 가로 4개에서 가장 큰 수 찾기
    for x in range(1,20):
        for y in range(0, 17):
            t = int(arr[x][y]) * int(arr[x][y+1]) * int(arr[x][y+2]) * int(arr[x][y+3])
            # print(int(arr[x][y]), int(arr[x][y+1]), int(arr[x][y+2]), int(arr[x][y+3]))
            if t > max_horz:
                max_horz = t
                max_horz_semi_arr = []
                max_horz_semi_arr.append([arr[x][y], arr[x][y+1], arr[x][y+2], arr[x][y+3]])
                max_horz_arr = max_horz_semi_arr[len(max_horz_semi_arr)-1]

    # 세로 4개에서 가장 큰 수 찾기
    for a in range(0,17):
        for b in range(1,20):
            t = int(arr[a][b]) * int(arr[a+1][b]) * int(arr[a+2][b]) * int(arr[a+3][b])
            if t > max_vert:
                max_vert = t
                max_vert_semi_arr = []
                max_vert_semi_arr.append([arr[a][b], arr[a+1][b], arr[a+2][b], arr[a+3][b]])
                max_vert_arr = max_vert_semi_arr[len(max_vert_semi_arr)-1]
    
    for h in range(1,17): # rd => 오른쪽 아래로 가는 대각선
        for i in range(0,17):
            t = int(arr[h][i]) * int(arr[h+1][i+1]) * int(arr[h+2][i+2]) * int(arr[h+3][i+3])
            if t > max_diag_rd:
                max_diag_rd = t
                max_diag_rd_semi_arr = []
                max_diag_rd_semi_arr.append([arr[h][i], arr[h+1][i+1], arr[h+2][i+2], arr[h+3][i+3]])
                max_diag_rd_arr = max_diag_rd_semi_arr[len(max_diag_rd_semi_arr)-1]

    for m in range(4,20):
        for n in range(0,17):
            t = int(arr[m][n]) * int(arr[m-1][n+1]) * int(arr[m-2][n+2]) * int(arr[m-3][n+3])
            if t > max_diag_ld:
                max_diag_ld = t
                max_diag_ld_semi_arr = []
                max_diag_ld_semi_arr.append([arr[m][n], arr[m-1][n-1], arr[m-2][n-2], arr[m-3][n-3]])
                max_diag_ld_arr = max_diag_ld_semi_arr[len(max_diag_ld_semi_arr)-1]
    
    print(max_horz)
    print(max_horz_arr)
    print(max_vert)
    print(max_vert_arr)
    print(max_diag_rd)
    print(max_diag_rd_arr)
    print(max_diag_ld)
    print(max_diag_ld_arr)

    res_arr = []
    res_arr.append(max_horz)
    res_arr.append(max_vert)
    res_arr.append(max_diag_rd)
    res_arr.append(max_diag_ld)

    res_arr.sort()
    print("\nThe largest product: ", res_arr[len(res_arr)-1])

euler()

# 70600674
import functools
from types import NoneType #used to cache calculated functions

@functools.lru_cache(None)

# 9 개수 늘려가며 나눠지는 수 구하기 10^n-1 꼴로
def nine_digit_N(n):
    for digit in range(1,1000):
        if ((pow(10,digit)-1)%n == 0):
            return digit
    return 0

max_len = 0
max_len_X = 0
for x in range(1,1000):
    if (nine_digit_N(x) > max_len):
        max_len = nine_digit_N(x)
        max_len_X = x
print("longest recurring cycle in decimal fraction part: \n",max_len,"\nd: \n",max_len_X)

# 9의 개수를 늘려가며 나눈 나머지가 0인 수를 찾게 되면, 순환 소수의 마디가 된다.
# 분모를 999...99 꼴로 만들었을때 길이가 n이면, 순환마디가 n이된다.
wordy = [
  "",
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
  "ten",
  "eleven",
  "twelve",
  "thirteen",
  "fourteen",
  "fifteen",
  "sixteen",
  "seventeen",
  "eighteen",
  "nineteen",
  "twenty"
]

decadey = [
  "",
  "",
  "twenty",
  "thirty",
  "forty", # 40의 정확한 spelling은 forty 이다... -> 처음에 fourty로 해서 답이 21224가 나왔었다...
  "fifty",
  "sixty",
  "seventy",
  "eighty",
  "ninety"
]

res = 0

def euler():
  global res
  for x in range(1,20):
    print(wordy[x], len(wordy[x]))
    res += len(wordy[x])
  for y in range(20,100):
    wort = decadey[y//10] + wordy[y%10]
    print(wort, len(wort))
    res += len(wort)
  for z in range(100, 1000):
    if z % 100 == 0:
      hundword = wordy[z//100] + "hundred"
    elif int(str(z)[1:])//10 <= 1:
      hundword = wordy[z//100] + "hundredand" + decadey[int(str(z)[1:])//10] + wordy[int(str(z)[1:])]
    else:
      hundword = wordy[z//100] + "hundredand" + decadey[int(str(z)[1:])//10] + wordy[int(str(z)[2])]
    print(hundword, len(hundword))
    res += len(hundword)
  print("onethousand", len("onethousand"))
  res += len("onethousand")
  print("result : ", res)

euler()

# 21124
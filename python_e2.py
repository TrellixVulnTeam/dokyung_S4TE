print("pizza"*10)

f = 50
c = (f - 32) / 1.8
print(c)

name = "파이썬"
birth = "2014년 12월 12일"
number = "20141212-1623210"
print(name + ' ' + birth + ' ' + number)

s = 'Daum KaKao'
a = s[:4]
b = s[5:]
s = b + ' ' + a
print(s)

naver_end_price = ['474,500', '461,500', '501,000', '500,500', '488,500']
print(max(naver_end_price))
print(min(naver_end_price))
print(naver_end_price[2])

naver_end_price2 = {'09/07': 474500, '09/08': 461500, '09/09': 501000, '09/10': 500500, '09/11': 488500}
print(naver_end_price2['09/09'])


# 4-1
print('*', end=' ')

# 4-2
for j in range(4):
    for i in range(5):
        print('*', end='')
    print('')
    # 4-3
x = int(input("숫자를 입력하세요: "))

for j in range(x):
    for i in range(j+1):
        print('*', end='')
    for i in range(x-j):
        print(' ', end='')
    print('')

j = input('숫자를 입력하세요: ')
x = int(j) * 2

for i in range(1, x):
	if i <= (x / 2):
		if i % 2 == 0:
			i += 1
		else:
			a = ' ' * ((int(j) - i) // 2) + '*' * i  
			print(a)
	else:
		if i % 2 == 0:
			i += 1
		else:			
			b = ' ' * ((int(j) - (x - i)) // 2) + '*' * (x - i)
			print(b)
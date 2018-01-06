i_max = int(input('피보나치 몇까지 ? : '))

fibo = [1, 1]

if i_max <= 2:
    fibo = fibo[:i_max]
else:
    for i in range(i_max-2):
        new_value = fibo[-2] + fibo[-1]
        fibo.append(new_value)

print(fibo)

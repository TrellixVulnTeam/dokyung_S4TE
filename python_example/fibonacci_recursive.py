fibo = {'1': 1, '2': 1}


def fibonacci(n):
    if str(n) not in fibo:
        fibo[str(n)] = fibonacci(n-2) + fibonacci(n-1)
    return fibo[str(n)]


if __name__ == '__main__':
    i = int(input('피보나치 몇까지? : '))
    print(fibonacci(i))

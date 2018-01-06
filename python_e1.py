def print_star(i, j):
    blank = (j - i) // 2
    star = i
    print(' ' * blank + '*' * star)


def main():
    j = int(input('숫자를 입력하세요: '))
    if j % 2 == 0:
        j -= 1

    for i in range(1, j, 2):
        print_star(i, j)

    for i in range(j, 0, -2):
        print_star(i, j)


if __name__ == '__main__':
    main()

#Write a program to display pattern
#                   A
#               B   A   B
#           C   B   A   B   C
#       D   C   B   A   B   C   D


def print_pattern(n):
    count = 0

    for i in range(1, n + 1):
        char_cnt = 1
        num = ord('A') + i - 1
        for j in range(n - i):
            print(" ", end="   ")
        for j in range(i + count):
            print(chr(num), end="   ")

            if char_cnt >= i:
                num = num + 1
            else:
                num = num - 1
            char_cnt = char_cnt + 1

        count = count + 1
        print("")


def main():
    row = int(input("Enter no. of rows:"))
    print_pattern(row)


if __name__ == '__main__':
    main()

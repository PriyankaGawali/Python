# Write a program to display pattern
# *  *   *   *   *   *   *
# *  *   *       *   *   *
# *  *               *   *
# *                      *


def print_pattern(n):
    col = (n * 2) - 1
    sp = -1
    for i in range(1, n + 1):
        char_cnt = 1
        for j in range(n + 1, i, -1):
            print("*", end="  ")
            char_cnt = char_cnt + 1

        for j in range(sp):
            print(" ", end="  ")
            char_cnt = char_cnt + 1
        sp = sp + 2

        while char_cnt <= col:
            print("*", end="  ")
            char_cnt = char_cnt + 1

        print(" ")


def main():
    row = int(input("Enter no. of rows:"))
    print_pattern(row)


if __name__ == '__main__':
    main()

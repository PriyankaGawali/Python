#WAP to display pattern
#                *
#           *    *     *
#       *   *    *     *    *
#   *   *   *    *     *    *   *


def print_pattern(n):
    count = 0
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="   ")
        for j in range(i + count):
            print("*", end="   ")
        count = count + 1
        print("")


def main():
    row = int(input("Enter no. of rows:"))
    print_pattern(row)


if __name__ == '__main__':
    main()




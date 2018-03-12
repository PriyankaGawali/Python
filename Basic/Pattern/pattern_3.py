#Writte a program to display pattern
#*   *   *   *
#    *   *   *
#        *   *
#            *


def print_pattern(n):
    for i in range(0, n):
        for j in range(i):
            print(" ", end="  ")
        for j in range(n - i):
            print("*", end="  ")
        print("")


def main():
    row = int(input("Enter no. of rows:"))
    print_pattern(row)


if __name__ == '__main__':
    main()

#Write a program to display pattern
#*  *   *   *
#*  *   *
#*  *
#*


def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(n + 1, i, -1):
            print("*", end="  ")

        print("")
def main():
    row = int(input("Enter no. of rows:"))
    print_pattern(row)


if __name__ == '__main__':
    main()

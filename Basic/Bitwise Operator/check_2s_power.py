# WAP to check the given no. is 2's number or not without using arithmatic operator
# Hint1 : Any 2's power has only one 1 bit
# Hint2 : num & num - 1 = 0


def check_2s_power(n):
    if n & (n - 1) == 0:
        return 1
    else:
        return 0


def main():
    num = int(input("Enter number : "))
    if check_2s_power(num):
        print(num, " is 2's power")
    else:
        print(num, " is not 2's power")


if __name__ == '__main__':
    main()

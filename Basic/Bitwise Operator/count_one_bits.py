# WAP to accept number from user & count number of 1s bit in given number.


def count_one_bits(n):
    x = 1
    count = 0
    while x <= n:
        if n & x != 0:
            count = count + 1
        x = x << 1

    return count


def main():
    num = int(input("Enter number : "))
    print("Number of 1 bits :", count_one_bits(num))


if __name__ == '__main__':
    main()

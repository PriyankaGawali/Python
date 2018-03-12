# WAP list comprehension to generate tables for the given range.


def main():
    lb = int(input("Enter lower bound : "))
    ub = int(input("Enter upper bound : "))
    print([[x * i for i in range(1, 11)] for x in range(lb, ub + 1)])


if __name__ == '__main__':
    main()

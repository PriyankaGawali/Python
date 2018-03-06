# WAP to accept a no. from user and check if it is special no. or not
# sum of factorial of digits = no.
# e.g 145= 1 + 24 + 120


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def is_special(n):
    num = n
    fact_sum = 0
    while num != 0:
        digit = num % 10
        fact_sum = fact_sum + factorial(digit)
        num = num / 10
        num = int(num)

    if fact_sum == n:
        return 1
    else:
        return 0


def main():
    num = int(input("Enter number :"))
    if is_special(num):
        print(num, " is special number")
    else:
        print(num, " is not special number")


if __name__ == '__main__':
    main()

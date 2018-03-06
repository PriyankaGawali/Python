# WAP to accept a number from user & display  factorial.


def factorial(n):
    ans = 1
    for i in range(n, 0, -1):
        ans = ans * i

    return ans


def main():
    num = int(input("Enter number:"))
    print("Factorial of ", num, " is ", factorial(num))


if __name__ == '__main__':
    main()

# WAP to accept a number from user & display recursive factorial.


def recursive_func_fact(n):
    if n != 1:
        ans = n * recursive_func_fact(n - 1)
    else:
        return 1

    return ans


def main():
    num = int(input("Enter number : "))
    print("Factorial of ", num, " is ", recursive_func_fact(num))


if __name__ == '__main__':
    main()

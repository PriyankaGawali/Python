#WAP to accept a number from user and check if it is palindrome or not


def check_palindrome(x):
    num = x
    rev = 0
    while x != 0:
        digit = x % 10
        rev = rev * 10 + digit
        x = int(x / 10)

    if rev == num:
        return True
    else:
        return False


def main():
    n = int(input("Enter number:"))
    if check_palindrome(n):
        print(n, " is palindrome number")
    else:
        print(n, " is not palindrome number")


if __name__ == '__main__':
    main()

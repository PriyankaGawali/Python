# Write a program to find out GCD of 2 numbers.
# Hint: 10&25 GCD=5


def find_gcd(a, b):
    i = 1
    gcd = 1
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            gcd = i
        i = i + 1

    return gcd


def main():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    print("GCD of ", num1, " and ", num2, " is :", find_gcd(num1, num2))


if __name__ == '__main__':
    main()

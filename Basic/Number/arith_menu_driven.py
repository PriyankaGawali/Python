# Write a program to perform menu driven arithmetic operation.


import sys


def print_menu_list():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Remainder")
    print("6.Exit")


def addition(a,b):
    return a + b


def subtraction(a,b):
    return a - b


def multiplication(a,b):
    return a * b


def division(a,b):
    return a / b


def remainder(a,b):
    return a % b


def main():
    print_menu_list()
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    choice = int(input("Enter choice:"))

    if choice == 1:
        print("Addition = ", addition(a, b))
        main()
    elif choice == 2:
        print("Subtraction = ", subtraction(a, b))
        main()
    elif choice == 3:
        print("Multiplication = ", multiplication(a, b))
        main()
    elif choice == 4:
        print("Division = ", division(a, b))
        main()
    elif choice == 5:
        print("Remainder = ", remainder(a, b))
        main()
    elif choice == 6:
        sys.exit()
    else:
        print("Invalid choice")
        main()


if __name__ == '__main__':
    main()

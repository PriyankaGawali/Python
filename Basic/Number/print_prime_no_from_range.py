# Write a program to accept a range from user and print all prime numbers from range
import math


def is_prime(num):
    if num < 0:
        num = num * -1

    if num % 2 == 0:
        return False

    for x in range(3, int(math.sqrt(num)) + 1,2):
        if num % x == 0:
            return False

    return True


def main():
    start_range = int(input("Enter start value:"))
    end_range = int(input("Enter end value:"))
    print("Prime numbers within range are:")
    if start_range < end_range:
        for x in range(start_range,end_range):
            if is_prime(x):
                print(x)

    else:
        print("Start value is greater than end value")


if __name__ == '__main__':
    main()

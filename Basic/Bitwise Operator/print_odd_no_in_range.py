# Write a program to accept a range from user and print all odd numbers in the range
# Hint: Don't use any arithmetic operator. Use bitwise operator. Do validation for upper & lower numbers


def is_odd(num):
    # return num % 2 == 1
    return num & 1 == 1


def main():
    start_range = int(input("Enter start value:"))
    end_range = int(input("Enter end value:"))
    print("Odd numbers in the given range are:")
    if start_range < end_range:
        for x in range(start_range,end_range):
            if is_odd(x):
                print(x)

    else:
        print("Start value is greater than end value")


if __name__ == '__main__':
    main()

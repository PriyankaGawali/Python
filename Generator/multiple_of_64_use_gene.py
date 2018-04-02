# Write a generator. It returns multiple of 64 in the given range.


def multiple_of_64(lb, ub):
    for num in range(lb, ub + 1):
        if num & 63 == 0:
            yield num


def main():
    lb = int(input("Enter start range:"))
    ub = int(input("Enter end range:"))
    print("Multiple of 64 in given range:")
    result = multiple_of_64(lb, ub)

    for value in result:
        print(value)

if __name__ == '__main__':
    main()

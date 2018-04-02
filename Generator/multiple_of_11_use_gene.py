# Write a generator which generates multiple of 11 until  max range.
# the divisibility of 11 is the difference between the sum of even position digits and sum of odd position digits is divisible by 11


def multiple_of_11_generator(min_range, max_range):
    for num in range(min_range, max_range + 1):
        sum1 = 0
        sum2 = 0
        cnt = 0
        n = num
        while n != 0:
            d = n % 10
            if cnt % 2 == 0:
                sum1 = sum1 + d
            else:
                sum2 = sum2 + d
            cnt = cnt + 1
            n = int(n / 10)

        diff = sum1 - sum2
        if diff < 0:
            diff = diff * (-1)
        if diff % 11 == 0:
            yield num


def main():
    min_range = int(input("Enter start range:"))
    max_range = int(input("Enter end range:"))
    print("Multiples of 11 in given range are:")
    result = multiple_of_11_generator(min_range, max_range)

    for value in result:
        print(value)


if __name__ == '__main__':
    main()

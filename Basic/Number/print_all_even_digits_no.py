# WAP to accept a range from user and print all even digits number in the range


def is_all_digits_even(number):
    while number:
        digit = number % 10
        if digit & 1 == 1:
            return False
        number = number // 10
    return True


def even_digits_number_in_range(lb, ub):
    result = []
    for number in range(lb, ub+1):
        if is_all_digits_even(number):
            result.append(number)
    print(result)


if __name__ == "__main__":
    print("Program to print list of even digits numbers in the given range....")
    lb = int(input("Enter lower bound of the range:"))
    ub = int(input("Enter upper boung of the range:"))
    even_digits_number_in_range(lb, ub)

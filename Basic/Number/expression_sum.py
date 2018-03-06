# WAP which computes value of following expression(for single digit 1- 9)
# a + aa + aaa + aaaa + .............
# 5 + 55 + 555 + 5555 + .............


def sum_of_terms(digit, terms):
    add = digit
    n = 1
    first_term = 1
    second_term = 10
    while n <= terms - 1:
        add = add + digit * first_term + digit * second_term
        first_term = first_term * 10 + 1
        second_term = second_term * 10
        n = n + 1

    return add


def main():
    digit = int(input("Enter digit :"))
    no_of_terms = int(input("Enter number of terms :"))
    print("Sum :", sum_of_terms(digit, no_of_terms))


if __name__ == '__main__':
    main()


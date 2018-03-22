'''
A number is said to be a Magic number if the sum of its digits is calculated repeatedly till a
single digit obtained and that single digit is 1.

WAP to check whether given no. is magic no. or not
For n = 199, Sum of digits = 1 + 9 + 9 = 19,
Sum of digits of 19 = 1 + 9 = 10
Sum of digits of 10 = 1 + 0 = 1
'''

# n = 199     199 > 0   add = 9    n = 19
# add = 9 + 9 =18       n = 1
# add = 19  n = 0


def is_magic(n):

    add = 0
    while n > 0 or add > 9:
        if n == 0:
            n = add
            add = 0

        digit = n % 10
        add = add + digit
        n /= 10
        n = int(n)

    if add == 1:
        return 1
    else:
        return 0




def main():
    n = int(input("Enter n:"))
    print(is_magic(n))

if __name__ == '__main__':
    main()

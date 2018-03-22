'''
Given an integer N, find whether N is a Disarium or not.
 The function should returns 1 if N is Disarium number else 0.

Input
    135
Output
    1
For 135, sum of digits powered with their respective position = 1^1 + 3^2 + 5^3 = 135, which is equal to an original number called as Disarium number.

'''


def is_disarinum_no(n):

    # count digits
    cnt = 0
    m = n1 = n
    while m != 0:
        d = m % 10
        cnt = cnt + 1
        m = m / 10
        m = int(m)

    ans = 0
    while n != 0:
        d = n % 10
        ans = ans + d ** cnt
        cnt = cnt - 1
        n = n / 10
        n = int(n)

    print(ans, n1)

    if n1 == ans:
        return 1
    else:
        return 0




def main():
    n = int(input("Enter n:"))
    print(is_disarinum_no(n))


if __name__ == '__main__':
    main()

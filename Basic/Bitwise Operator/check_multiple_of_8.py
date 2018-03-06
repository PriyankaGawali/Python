# Write a program to accept number from user and check if it is multiple
# of 8 (without using any arithmetic operators).
# Hint: If last 3 bits are 0, then it is multiple of 8.
# If any of the last 3 bits is not 0, then it is not multiple of 8.
# Also, we need to & with (2^3 - 1). Because we need 111, and logic is
# if we want all 1s then (2^no.-1) will give those many 1s.

# Pattern:
# 8    ->      1 000
# 16    ->    10 000
# 24    ->    11 000
# 48    ->   110 000
# 56    ->   111 000
# 64    ->  1000 000


def multiple_of_8(no):
    return no & ((2 ^ 3) - 1) == 0


def main():
    num = int(input("Enter number : "))
    if multiple_of_8(num):
        print(num, " is multiple of 8")
    else:
        print(num, " is not multiple of 8")


if __name__ == '__main__':
    main()

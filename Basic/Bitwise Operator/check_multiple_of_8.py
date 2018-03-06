''' Write a program to accept number from user and check if it is multiple
# of 8 (without using any arithmetic operators).
# Hint: If last 3 bits are 0, then it is multiple of 8.
'''

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

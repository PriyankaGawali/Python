''' Write a program to perform menu driven bitwise operator operation.
 Menu 1. Turn off respective position
 2. Turn on respective position
 3. Toggle respective position
 4. Exit    '''


import sys


def turn_off_respective_position(n, pos, bits):
    if bits <= pos:
        x = (1 << bits) - 1
        x = x << (pos - bits)
        x = ~x
        return n & x
    return -1


def turn_on_respective_position(n, pos, bits):
    if bits <= pos:
        x = (1 << bits) - 1
        x = x << (pos - bits)
        #x = ~x
        return n | x
    return -1


def toggle_respective_position(n, pos, bits):
    if bits <= pos:
        x = (1 << bits) - 1
        x = x << (pos - bits)
        return n ^ x
    return -1


def main():
    num = int(input("Enter number : "))
    while True:
        print("Menu")
        print("1. Turn off respective position")
        print("3. Turn on respective position")
        print("3. Toggle respective position")
        print("4. Exit")
        choice = int(input("Enter choice : "))

        if choice == 1:
            position = int(input("Enter position : "))
            no_of_bits = int(input("Enter no. of bits : "))
            print("After turn off respective position : ",turn_off_respective_position(num, position, no_of_bits))

        elif choice == 2:
            position = int(input("Enter position : "))
            no_of_bits = int(input("Enter no. of bits : "))
            print("After turn off respective position : ",turn_on_respective_position(num, position, no_of_bits))

        elif choice == 3:
            position = int(input("Enter position : "))
            no_of_bits = int(input("Enter no. of bits : "))
            print("After toggle respective position : ", toggle_respective_position(num, position, no_of_bits))

        elif choice == 4:
            sys.exit()


if __name__ == '__main__':
    main()

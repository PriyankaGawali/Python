'''WAP to accept a number , position and no. of bits to be turn off from given position.
Turn off respective bits from the given position and display the result.
'''


def turn_off_respective_position(n, pos, bits):
    if bits < pos:
        x = (1 << bits) - 1
        x = x << (pos - bits)
        x = ~x
        return n & x
    return -1



def main():
    num = int(input("Enter number : "))
    position = int(input("Enter position : "))
    no_of_bits = int(input("Enter no. of bits : "))
    print("After turn off respective position : ",turn_off_respective_position(num, position, no_of_bits))


if __name__ == '__main__':
    main()

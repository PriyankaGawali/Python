#WAP to accept a number , position and no. of bits to be turn off from given position.
#Turn off respective bits from the given position and display the result.
#     011011010   = 218
#pos= 5 from position 5
#no. of bits 4
#Ans  011000000   =  192

#step 1 - position must be greater than no. of bits
#step 2 - find x    ---->2^4 -1,    1<<num & bit - 1
#left shift by pos - no. of bits


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

'''WAP to accept 2 strings from user. And check if second string is a right rotation of first string.
 Hint:
 India, iaInd -> This should be true
 Jeetendra 1st right rotation "aJeetendr"   '''


def is_rotation(input_str,validate_str):
    if len(input_str) == len(validate_str):
        return validate_str in input_str + input_str
    return False


def main():
    input_str = input("Enter string:")
    validate_str = input("Enter validate string:")
    if is_rotation(input_str,validate_str):
        print("{} is right rotation of {}".format(validate_str, input_str))
    else:
        print("{} is not right rotation of {}".format(validate_str, input_str))


if __name__ == '__main__':
    main()

# WAP to print alternate character start with first character


def print_alternate_char(input_string):
    len_input_str = len(input_string)
    i = 0
    print("Alternate characters are:")
    while i < len_input_str:
        print(input_string[i])
        i = i + 2


def main():
    input_str = input("Enter string:")
    print_alternate_char(input_str)


if __name__ == '__main__':
    main()

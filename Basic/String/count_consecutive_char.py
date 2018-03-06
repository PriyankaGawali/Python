# WAP to count how many times a character is consecutive
# input - aabbcccddabbb
# output - a2b2c3d2a1b3


def count_consecutive(input_str):
    result_str = " "
    i = 0
    while i < len(input_str):
        count = 1
        char_to_check = input_str[i]
        while i + 1 < len(input_str) and input_str[i + 1] == char_to_check:
            count += 1
            i += 1

        result_str += char_to_check + str(count)
        i += 1

    return result_str


def main():
    str_a = input("Enter string : ")
    print("Output is : ", count_consecutive(str_a))


if __name__ == '__main__':
    main()

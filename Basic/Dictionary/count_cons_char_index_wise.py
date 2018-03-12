# WAP to count how many times a character is consecutive
# input - aabbbccddabbb
# output - {a: {0 : 2, 9: 1},
#           b: {2 : 3, 10 : 3},
#           c: {5 : 2},
#           d: {8 : 2}


def count_cons_char_index_wise(input_str):
    result_dict = {}

    i = 0
    while i < len(input_str):
        char_to_check = input_str[i]

        if char_to_check in result_dict:
            ans_dict = result_dict[char_to_check]
        else:
            ans_dict = {}

        count = 1

        index = i
        while i + 1 < len(input_str) and input_str[i + 1] == char_to_check:
            count += 1
            i += 1

        ans_dict[index] = count


        result_dict[char_to_check] = ans_dict
        i = i + 1

    return result_dict


def main():
    input_str = input("Enter string : ")
    print(count_cons_char_index_wise(input_str))


if __name__ == '__main__':
    main()

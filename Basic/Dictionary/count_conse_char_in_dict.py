# WAP to count how many times a character is consecutive
# input - aabbcccddab
# output - {a:3, b:3, c:3, d:2 }


def generate_dict_of_count(input_str):
    ans_dict = {}
    i = 0
    while i < len(input_str):
        count = 0
        char_to_check = input_str[i]
        for ch in input_str:
            if ch == input_str[i]:
                count += 1

        ans_dict[char_to_check] = count
        i = i + 1

    return ans_dict


def main():
    input_str = input("Enter string : ")
    ans_dict = generate_dict_of_count(input_str)
    print(ans_dict)


if __name__ == '__main__':
    main()

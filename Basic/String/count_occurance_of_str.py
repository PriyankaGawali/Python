# WAP to accept two strings and without using count method,count the occurances of first string into second string


def count_occurance(input_str,sub_str):
    input_str = input_str.lower()
    sub_str = sub_str.lower()
    input_str_len = len(input_str)
    sub_str_len = len(sub_str)
    i = 0
    count = 0
    while i < input_str_len:
        if input_str[i:i + sub_str_len] == sub_str:
            count = count + 1
        i = i + 1

    return count


def main():
    input_string = input("Enter string:")
    sub_string = input("Enter sub string:")
    print("%s is occured %d times in %s" % (sub_string, count_occurance(input_string, sub_string), input_string))


if __name__ == '__main__':
    main()

# WAP which implements findall() method.

import re


def find_all(pattern, input_str):

    result = []
    index = 0
    x = re.search(pattern, input_str)
    while x != None:
        result.append((x.start() + index, x.end() + index))
        index = x.end()
        # index = index + x.end()
        input_str = input_str[x.end():]
        x = re.search(pattern, input_str)

    return result


def main():
    input_str = input("Enter string :")
    pattern = input("Enter pattern :")
    print(find_all(pattern, input_str))


if __name__ == '__main__':
    main()

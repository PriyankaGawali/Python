# WAP to accept pattern and string from user and count occurances of the given pattern in the string using search method


import re


def main():
    count = 0
    pattern = input("Enter pattern :")
    input_string = input("Enter string :")
    ans = re.search(pattern, input_string)
    while ans != None:
        count = count + 1
        index = ans.end()
        input_string = input_string[index:]
        ans = re.search(pattern, input_string)

    print("Count :", count)


if __name__ == '__main__':
    main()

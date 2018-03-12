# WAP to accept an alphanumeric string from user and remove all the characters other than digits from it
# \D :Matches any non-digit character; this is equivalent to the class [^0-9].


import re

def main():
    input_string = input("Enter string :")
    print(re.sub("\D", "", input_string))


if __name__ == '__main__':
    main()

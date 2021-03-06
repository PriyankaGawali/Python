# Write a program to accept a string from user. Check whether string is palindrome or not.


def is_palindrome(input_str):
    i = 0
    j = len(input_str) - 1
    input_str = input_str.lower()
    while i <= j:
        if input_str[i] != input_str[j]:
            return False

        i = i + 1
        j = j - 1

    return True


def main():
    input_str = input("Enter string : ")
    if is_palindrome(input_str):
        print(input_str, " is palindrome string")
    else:
        print(input_str, " is not palindrome string")


if __name__ == '__main__':
    main()

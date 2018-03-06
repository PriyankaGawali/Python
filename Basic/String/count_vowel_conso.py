#Write a program to accept a string from user and print how many (count) vowels and consonants present in that string.

import string


def count_vowel_consonant(str_a):
    vowel_cnt = 0
    cons_cnt = 0
    str_a = str_a.lower()
    for x in str_a:
        if x in list(string.ascii_lowercase):  # It contains 'a' to 'z' characters
            if x in ['a', 'e', 'i', 'o', 'u']:
                vowel_cnt = vowel_cnt + 1
            else:
                cons_cnt = cons_cnt + 1

    print("Vowel count :",vowel_cnt)
    print("Consonant count :",cons_cnt)


def main():
    str_a = input("Enter string to count vowels and consonants:")
    count_vowel_consonant(str_a)


if __name__ == "__main__":
    main()


''' WAP to accept a sentence from user and print count of characters , words in the input statement
Input: Enter string:Hi.........hi Priya
      Enter sub string:hi
      
Output: hi is occured 2 times in Hi.........hi Priya

'''


def count_char_words(string):
    char_cnt = 0
    word_cnt = 1
    for ch in string:
        char_cnt = char_cnt + 1
        if ch == ' ' or ch == '\t':
            word_cnt = word_cnt + 1

    print("Number of characters : ", char_cnt)
    print("Number of words : ", word_cnt)


def main():
    sentence = input("Enter sentence to count characters and words:")
    count_char_words(sentence)


if __name__ == '__main__':
    main()

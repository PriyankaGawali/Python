# WAP to accept name of a file from user & display longest & smallest line from the same.


import sys


def find_large_small_line(fd):
    large_line_len = 0
    large_line = ""
    small_line = ""
    small_line_len = sys.maxsize
    for line in fd:

        if len(line) > large_line_len:
            large_line_len = len(line)
            large_line = line

        if len(line) < small_line_len and len(line) != 1:
            small_line_len = len(line)
            small_line = line

    print("Largest line : ", large_line)

    print("Smallest line : ", small_line)


def main():
    file_name = input("Enter file name to open :")
    fd = open(file_name)

    # Another way to find largest and smallest line from file
    # print("Largest line : ", max(open(file_name, 'r'), key=len))
    # print("Smallest line : ", min(open(file_name, 'r'), key=len))
    find_large_small_line(fd)


if __name__ == '__main__':
    main()

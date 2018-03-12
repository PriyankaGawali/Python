# WAP to implement readlines(fd,no_of_lines) method which takes argument as file discriptor, no. of lines to read.


def read_no_of_lines(fd,no_of_lines):
    i = 0
    while i < no_of_lines:
        line = fd.readline()
        print(line)
        i = i + 1


def main():
    file_name = input("Enter file name to open :")
    fd = open(file_name)
    print("File is opened.")
    no_of_lines = int(input("How many lines you want to read : "))
    read_no_of_lines(fd,no_of_lines)


if __name__ == '__main__':
    main()

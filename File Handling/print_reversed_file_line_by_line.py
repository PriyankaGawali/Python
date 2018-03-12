''' WAP accept file name from user and display file in reverse order without using loop, readlines and built in container(don't use list)
 use seek ,use recursive program
 works on bytes
 FIle i/p
 hi
 hello
 bye

 o/p
 bye
 hello 
 hi
'''

def reverse_line_display(fd):
    line = fd.readline()
    if line == "":
        return

    reverse_line_display(fd)
    print(line)


def main():
    file_name = input("Enter file name to open :")
    fd = open(file_name, "r")
    reverse_line_display(fd)


if __name__ == '__main__':
    main()
